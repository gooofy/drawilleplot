#!/usr/bin/env python
from setuptools import setup

project = "drawilleplot"
version = "0.1.0"

setup(
    name=project,
    version=version,
    description="matplotlib backend for graph output in unicode terminals using drawille",
    author="Guenter Bartsch",
    author_email="guenter@zamia.org",
    url="https://github.com/gooofy/drawilleplot",
    packages=["drawilleplot"],
    download_url="https://github.com/gooofy/drawilleplot.git",
    license="Apache",
    platforms=["any"],
    long_description="""
    matplotlib backend for graph output in unicode terminals using drawille
    """,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "drawille>=0.1.0",
        "matplotlib>=3.1.2",
    ],
)
