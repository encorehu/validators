#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='validators',
    version="0.1",
    author='encorehu',
    author_email='huyoo353@126.com',
    description='my python validators for string, email, phone, etc.',
    url='https://github.com/encorehu/validators',
    packages=find_packages(),
    package_dir={'validators':'validators'},
    package_data={'validators':['*.*',
        ]},
    zip_safe = False,
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
