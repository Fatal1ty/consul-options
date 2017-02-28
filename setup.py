#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='lazy-consul',
    version='0.1.1',
    description='Lazy client library for the Consul Key/Value store',
    platforms="all",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Clustering',
    ],
    license='MIT',
    author='Alexander Tikhonov',
    url='https://github.com/Fatal1ty/lazy-consul',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'python-consul'
    ]
)
