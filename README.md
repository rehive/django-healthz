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

4. Configure the readiness checks:

```
HEALTHCHECK = {
    'READINESS_CHECKS': ('databases', 'caches', 'queues',)
}
```

## TODO

1. Update responses to JSON
2. Allow customization or readiness and healthz URLs.

