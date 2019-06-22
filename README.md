# Rehive Django HealthCheck

## Quick start

1. Add "healthcheck" to your INSTALLED_APPS settings like this:

```
    INSTALLED_APPS = [
        ...
        'healthcheck',
    ]
```

2. Include the healtheck middleware in the django middleware:

```
MIDDLEWARE = [
    'healthcheck.middleware.HealthCheckMiddleware',
    ...
]
```

## TODO

1. Add support for celery/rabbitmq, cache checks etc.
2. Update responses to JSON
3. Allow customization or readiness and healthz URLs.
