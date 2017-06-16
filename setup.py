#!/usr/bin/env python

from setuptools import setup


setup(
    name='consul-options',
    version='0.8',
    description='Framework for using Consul as your project options storage',
    long_description=open('README.rst').read(),
    platforms="all",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
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
