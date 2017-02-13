#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: kakakaya, Date: Sat Feb  4 18:59:06 2017
from setuptools import setup, find_packages


setup(
    name="tweetsave",
    version="1.1.0",
    description='A Python3 library for https://tweetsave.com',
    author='kakakaya',
    author_email="kakakaya@gmail.com",
    url="https://github.com/kakakaya/tweetsave-python",
    license="MIT",
    packages=find_packages(),
    test_suite="nose.collector",
    entry_points={
        'console_scripts': 'tweetsave = tweetsave.cli:cli'
    },
    install_requires=[
        'requests',
        'click'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ]
)
