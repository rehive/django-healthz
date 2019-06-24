# Rehive Django HealthCheck

## Quick start

1. Install the package:

```
pip install django-healthz
```

2. Add "healthz" to your INSTALLED_APPS settings like this:

```
    INSTALLED_APPS = [
        ...
        'healthz',
    ]
```

3. Include the healtheck middleware in the django middleware:

```
MIDDLEWARE = [
    'healthz.middleware.HealthCheckMiddleware',
    ...
]
```

## TODO

1. Add support for celery/rabbitmq, cache checks etc.
2. Update responses to JSON
3. Allow customization or readiness and healthz URLs.
