#!/usr/bin/env python

import os

try:
    from setuptools import setup, Extension, Command
except ImportError:
    from distutils.core import setup, Extension, Command

import tempwork

dependencies = []

setup(
    name=tempwork.__name__,
    version=tempwork.__version__,
    description=tempwork.__description__,
    long_description=open('README.rst').read(),
    author=tempwork.__author__,
    author_email=tempwork.__author_email__,
    url=tempwork.__url__,
    license=tempwork.__license__,
    packages=['tempwork'],
    #test_suite='tests',
    install_requires=dependencies,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Database',
        'Topic :: Database :: Front-Ends'
    ],
    entry_points={
        'console_scripts': [
            'tempwork = tempwork.__main__:main',
        ],
    }
)
