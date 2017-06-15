#!/usr/bin/env python

from setuptools import setup

setup(
    name='lazy-consul',
    version='0.6',
    description='Lazy client library for the Consul Key/Value store',
    platforms="all",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Clustering',
    ],
    license='MIT',
    author='Alexander Tikhonov',
    url='https://github.com/Fatal1ty/lazy-consul',
    py_modules=['lazy_consul'],
    install_requires=[
        'python-consul',
        'six',
    ]
)
