#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dlvr
import os
from setuptools import setup, find_packages


## dependencies 
install_requires = [

]

packages = find_packages()

setup(
    name='dlvr',
    version=dlvr.__version__,
    author='Bernhard Maeser',
    author_email='bernhard.maeser@gmail.com',
    url='https://github.com/bmaeser/dlvr',
    license="MIT",
    scripts=['bin/dlvr'],
    description="A light wrapper around smtplib and email",
    long_description=open('README.rst').read(),
    packages = packages,
    include_package_data=True,
    install_requires = install_requires,
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Installation/Setup',
        'Operating System :: POSIX',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)

