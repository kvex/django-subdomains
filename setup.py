#!/usr/bin/env python
from setuptools import setup

install_requires = ['django']

setup(name='django-subdomains',
    version='1.2.1',
    url='http://github.com/tkaemming/django-subdomains/',
    author='ted kaemming',
    author_email='ted@kaemming.com',
    description="Subdomain tools for the Django framework, including "
        "subdomain-based URL routing.",
    packages=('subdomains',),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
    license='MIT License',
)
