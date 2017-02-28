#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='lazy-consul',
    version='0.1',
    description='Lazy client library for the Consul Key/Value store',
    platforms="all",
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
    ],
    author='Alexander Tikhonov',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'python-consul'
    ]
)
