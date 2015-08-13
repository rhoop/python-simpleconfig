#!/usr/bin/env python
__version__ = '0.1'
__author__ = 'Richard Hoop'

import sys

install_requires = ['configparser']

try:
    from setuptools import setup
except ImportError:
    print("python-simpleconfig needs setuptools in order to build. Install it using"
          " your package manager (usually python-setuptools) or via pip (pip"
          " install setuptools).")
    sys.exit(1)

setup(
    name='python-simpleconfig',
    version=__version__,
    description='Easy Python Configs',
    author=__author__,
    author_email='wrhoop@gmail.com',
    license='GPLv3',
    install_requires=install_requires,
    data_files=[],
    url="https://github.com/rhoop/python-simpleconfig",
    packages=['simpleconfig']
)
