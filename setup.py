#! /usr/bin/env python
import os
import schnipp_connector
from setuptools import setup, find_packages

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name='djpl-emailing',
    version='0.1',
    description='a django-productline feature to include schnipp.js',
    long_description=read('README.rst'),
    license='The MIT License',
    keywords='django, django-productline, email',
    author='Toni Michel',
    author_email='toni@schnapptack.de',
    url="https://github.com/tonimichel/djpl-emailing",
    packages=find_packages(),
    package_dir={'emailing': 'emailing'},
    include_package_data=True,
    scripts=[],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        'django-productline',
    ]
)

