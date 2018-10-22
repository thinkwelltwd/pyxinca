# -*- coding: utf-8 -*-
#!/usr/bin/python

import io
import re
import os
from os.path import dirname, join

from setuptools import setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

setup(
    name='pyxinca',
    version='0.1.0',
    license='MIT',
    description='Xinca MDM Client',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.md')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.md'))
    ),
    author='Dave Burkholder',
    author_email='dave@compassfoundation.io',
    url='https://code.compassfoundation.io/dave/pyxinca',
    packages=get_packages('pyxinca'),
    package_data=get_package_data('pyxinca'),
    zip_safe=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: SAP',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    keywords=[
        'Xinca', 'XincaMDM',
    ],
    install_requires=[
        'requests',
    ],

)
