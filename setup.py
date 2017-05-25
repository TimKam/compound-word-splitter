# -*- coding: utf-8 -*-

import codecs, setuptools


setuptools.setup(
    name='compound-word-splitter',
    packages=['splitter'],
    version='0.4',
    description='Splits compound words, like German "Effektivitätsberechnung',
    author='Timotheus Kampik',
    author_email='timotheus.kampik@gmail.com',
    url='https://github.com/TimKam/compound-word-splitter',
    platforms=["any"],
    license="MIT",
    zip_safe=False,
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Documentation",
    ],
    long_description=codecs.open("README.rst", "r", "utf-8").read(),
)