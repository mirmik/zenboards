#!/usr/bin/env python3

from wheel.bdist_wheel import bdist_wheel as bdist_wheel_
from setuptools import setup, Extension, Command
from distutils.util import get_platform

import zencad

import glob
import sys
import os

setup(
    name="zenboards",
    packages=["zenboards"],
    version="0.1.0",
    license="MIT",
    description="",
    author="mirmik",
    author_email="mirmikns@yandex.ru",
    url="https://github.com/mirmik/zenboards",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    keywords=["testing", "cad"],
    classifiers=[],
)
