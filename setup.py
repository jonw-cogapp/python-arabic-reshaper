#!/usr/bin/env python
# coding = utf-8

from setuptools import setup

setup(
    name = "arabic_reshaper",
    description = "Reconstruct Arabic sentences to be used in applications that don't support Arabic",
    version = '1.0.1',
    platforms = "ALL",
    license = "GPL",
    packages = ['arabic_reshaper'],
    install_requires = [],
    author = "Abdullah Diab",
    author_email = "mpcabd@gmail.com",
    maintainer = "Abdullah Diab",
    maintainer_email = "mpcabd@gmail.com",
    package_dir = { 'arabic_reshaper' : '.' },
    keywords = "arabic shaping reshaping reshaper",
    url = "https://mpcabd.xyz/python-arabic-text-reshaper/",
    download_url = "https://github.com/mpcabd/python-arabic-reshaper/tarball/master",
    classifiers = [
        "Natural Language :: Arabic",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
 )
