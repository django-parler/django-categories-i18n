#!/usr/bin/env python
import codecs
import os
import re
import sys
from os import path

from setuptools import find_packages, setup


def read(*parts):
    file_path = path.join(path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding="utf-8").read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError("Unable to find version string.")


setup(
    name="django-categories-i18n",
    version=find_version("categories_i18n", "__init__.py"),
    license="Apache 2.0",
    install_requires=[
        "django-mptt>=0.9.1",
        "django-parler>=2.0.1",
    ],
    requires=[
        "Django (>=2.2)",
    ],
    description="Translatable Categories model",
    long_description=read("README.rst"),
    author="Diederik van der Boor",
    author_email="opensource@edoburu.nl",
    url="https://github.com/django-parler/django-categories-i18n",
    download_url="https://github.com/django-parler/django-categories-i18n/zipball/master",
    packages=find_packages(exclude=("example*",)),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
