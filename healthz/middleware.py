from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotAllowed
from django.conf import settings
from logging import getLogger


logger = getLogger('django')


class HealthCheckMiddleware(MiddlewareMixin):
    readiness_checks = []

    def process_request(self, request):
        healthcheck = getattr(settings, 'HEALTHCHECK', None)
        if healthcheck:
            self.readiness_checks = healthcheck.get('READINESS_CHECKS', [])

        if request.path == "/readiness":
            return self.readiness(request)
        elif request.path == "/healthz":
            return self.healthz(request)

    def healthz(self, request):
        """
        Returns that the server is alive.
        """
        return HttpResponse("OK")

    def readiness(self, request):
        checks = []
        for check in self.readiness_checks:
            if check == 'databases':
                checks.append(self.databases_ok(request))
            if check == 'caches':
                checks.append(self.caches_ok(request))
            if check == 'queues':
                checks.append(self.queues_ok(request))
        if not all(checks):
            return HttpResponseServerError("DOWN")
        return HttpResponse("OK")

    def databases_ok(self, request):
        """
        Connect to each database and do a generic standard SQL query
        that doesn't write any data and doesn't depend on any tables
        being present.
        """
        try:
            from django.db import connections
        except ImportError as e:
            logger.exception(e)
            return False

        try:
            for name in connections:
                cursor = connections[name].cursor()
                cursor.execute("SELECT 1;")
                row = cursor.fetchone()
                if row is None:
                    return False
        except Exception as e:
            logger.exception(e)
            return False
        else:
            return True

    def caches_ok(self, request):
        try:
            from django_redis import get_redis_connection
            from redis.exceptions import ConnectionError
        except ImportError as e:
            logger.exception(e)
            return False

        try:
            return get_redis_connection("default").ping()
        except ConnectionError as e:
            logger.exception(e)
            return False

    def queues_ok(self, request):
        try:
            from celery import shared_task
        except ImportError as e:
            logger.exception(e)
            return False

        @shared_task(ignore_result=False)
        def add(x, y):
            return x + y

        try:
            result = add.apply_async(args=[1, 1], expires=3,)
            result.get(timeout=3)
            if result.result != 2:
                return False
            return True
        except Exception as e:
            logger.exception(e)
            return False

        return False
