#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

setup(
    name='kubetoken',
    version='0.1.0',
    description='Generate token-based kubeconfig for some service account',
    author='Weida Hong',
    author_email='wdhongtw@gmail.com',
    url='https://github.com/',
    license='MIT license',
    python_requires='>=3.5',
    install_requires=[
        'kubernetes',
        'PyYAML'
    ],
    setup_requires=[
        'wheel',
    ],
    package_dir={'': 'lib'},
    packages=[],
    py_modules=['kubetoken'],
    scripts=['bin/kubetoken']
)
