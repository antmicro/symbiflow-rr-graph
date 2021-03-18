#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2021  The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC


import setuptools


# Generate the version number
def scm_version():
    def local_scheme(version):
        if version.tag and not version.distance:
            return version.format_with("")
        else:
            return version.format_choice("+{node}", "+{node}.dirty")
    return {
        "relative_to": __file__,
        "version_scheme": "post-release",
        "local_scheme": local_scheme,
        "write_to": "rr_graph/version.py",
    }


# Read in the module description from the README.md file.
with open("README.md", "r") as fh:
    long_description = fh.read()


# Read in the setup_requires from the requirements.txt file.
setup_requires = []
with open('requirements.txt') as fh:
    for r in fh:
        if '#' in r:
            r = r[:r.find('#')]
        r = r.strip()
        if not r:
            continue
        if r not in ('-e .',):
            setup_requires.append(r)


setuptools.setup(
    name="rr-graph",
    use_scm_version=scm_version(),
    author="SymbiFlow Authors",
    author_email="symbiflow@lists.librecores.org",
    description="SymbiFlow RR Graph libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SymbiFlow/symbiflow-rr-graph",
    python_requires=">=3.7",
    packages=setuptools.find_packages(),
    include_package_data=True,
    setup_requires=setup_requires,
    install_requires=[
        "progressbar2",
        "simplejson",
        "pycapnp",
        "lxml",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License",
        "Operating System :: OS Independent",
    ],
)
