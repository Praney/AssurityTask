from setuptools import setup, find_packages
from os import path
setup(name = 'api-test',
version = '1.0',
description = 'Test Strategy for API test',
author = 'Praney Madan',
packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)