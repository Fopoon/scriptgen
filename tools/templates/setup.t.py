#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from setuptools import find_packages, setup

NAME = '${project_name}'
VERSION = '${version}'
DESCRIPTION = '${description}'
HOME = Path(__file__).parent
README = (HOME / '${readme_file}').read_text()
CHANGELOG = (HOME / '${changelog_file}').read_text()
AUTHOR = 'Elmer Nocon, fopoon'
AUTHOR_EMAIL = 'elmernocon@gmail.com'
LICENSE = '${license_type}'
PLATFORMS = 'Any'
URL = '${repo_link}'
DOWNLOAD_URL = 'https://pypi.org/project/${project_name}/'
CLASSIFIERS = [
    'Development Status :: ${python_development_status}',
    'License :: OSI Approved :: ${license_type} License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Operating System :: Unix',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3 :: Only',
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description='\n\n'.join([README, CHANGELOG]),
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    platforms=PLATFORMS,
    url=URL,
    download_url=DOWNLOAD_URL,
    classifiers=CLASSIFIERS,

    packages=find_packages(
        exclude=[
            "tests",
            "tests.*",
            "*.tests.*",
            "*.tests"
        ]
    ),
)
