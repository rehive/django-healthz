<p align="center">
  <img width="64" src="https://avatars2.githubusercontent.com/u/22204821?s=200&v=4" alt="Rehive Logo">
  <h1 align="center">Django Healthz</h1>
  <p align="center">Simple Django healthcheck middleware</p>
</p>

## Quick start

1. Install the package:

```sh
pip install django-healthz
```

2. Add "healthz" to your INSTALLED_APPS settings like this:

```python
INSTALLED_APPS = [
    ...
    'healthz',
]
```

3. Include the healtheck middleware in the django middleware:

```python
MIDDLEWARE = [
    'healthz.middleware.HealthCheckMiddleware',
    ...
]
```

4. Configure the readiness checks:

```python
HEALTHCHECK = {
    'READINESS_CHECKS': ('databases', 'caches', 'queues',)
}
```

## TODO

1. Update responses to JSON
2. Allow customization or readiness and healthz URLs.

