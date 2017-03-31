#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
setup(
    name='Flask-LoginManager',
    version='1.1.6',
    keywords=('flask', 'login', 'multiple roles', 'permissions'),
    description='Flask-Loginmanager supports multiple roles and permissions for Flask, inspired by Flask-Login',
    license='MIT',
    author='rain',
    author_email='rain@joymud.com',
    url='https://github.com/AristotleJunior/flask-loginmanager',
    platforms='any',
    packages=['flask_loginmanager'],
    install_requires=['Flask'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

