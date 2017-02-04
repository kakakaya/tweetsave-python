#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: kakakaya, Date: Sat Feb  4 18:59:06 2017
from setuptools import setup, find_packages


setup(
    name="tweetsave",
    version="1.0.0",
    description='A library for https://tweetsave.com',
    author='kakakaya',
    packages=find_packages(),
    test_suite="nose.collector",
    entry_points={
        'console_scripts': 'tweetsave = tweetsave.cli:cli'
    },
    install_requires=[
        'requests',
        'click'
    ],
)
