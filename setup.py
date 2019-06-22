import os
from codecs import open
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='rehive-django-healthcheck',
    version=open('VERSION').read().strip(),
    packages=find_packages(),
    include_package_data=True,
    description='Simple middleware for healthchecks',
    long_description=README,
    url='https://github.com/rehive/rehive-django-healthcheck',
    author='Rehive',
    author_email='info@rehive.com',
    install_requires=["Django>=2.0"],
    python_requires='>=3.4',
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
