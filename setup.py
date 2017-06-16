#!/usr/bin/env python

from setuptools import setup


setup(
    name='consul-options',
    version='0.7',
    description='Framework for using Consul as your project options storage',
    long_description=open('README.rst').read(),
    platforms="all",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Clustering',
    ],
    license='Apache License, Version 2.0',
    author='Alexander Tikhonov',
    author_email='random.gauss@gmail.com',
    url='https://github.com/Fatal1ty/consul-options',
    py_modules=['consul_options'],
    install_requires=[
        'python-consul',
        'six',
    ]
)
