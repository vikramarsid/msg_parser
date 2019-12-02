#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'msg_parser', '__version__.py'), 'r') as f:
    exec (f.read(), about)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as req_file:
    requirements = [l.strip('\n') for l in req_file if l.strip('\n') and not l.startswith('#')]

with open('requirements_dev.txt') as req_file:
    test_requirements = [l.strip('\n') for l in req_file if l.strip('\n') and not l.startswith('#')]

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Communications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    entry_points={
        'console_scripts': [
            'msg_parser=msg_parser.cli:main',
        ],
    },
    install_requires=requirements,
    license=about['__license__'],
    include_package_data=True,
    keywords='msg_parser',
    packages=find_packages(include=['msg_parser']),
    python_requires=">=3.4",
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False,
    extras_require={
        'rtf': ['compressed_rtf >= 1.0.5'],
    },
)
