# -*- coding: utf-8 -*-
#
# This file is part of DjangoRestAuth (https://django.restauth.net).
#
# DjangoRestAuth is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DjangoRestAuth is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DjangoRestAuth.  If not, see <http://www.gnu.org/licenses/>.

# breaks distutils in python2.7!
#from __future__ import unicode_literals

import os
import re
import shutil

from subprocess import Popen
from subprocess import PIPE

from distutils.command.clean import clean as _clean

try:
    from setuptools import Command
    from setuptools import setup
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import Command
    from setuptools import setup

requires = [
    'Django>=1.5.1',
    'RestAuthClient>=0.6.1',
]

LATEST_RELEASE = '0.0'


class clean(_clean):
    def initialize_options(self):
        _clean.initialize_options(self)

    def run(self):
        _clean.run(self)

        # clean sphinx documentation:
        cmd = ['make', '-C', 'doc', 'clean']
        p = Popen(cmd)
        p.communicate()

        coverage = os.path.join('doc', 'coverage')
        generated = os.path.join('doc', 'gen')

        if os.path.exists(coverage):
            print('rm -r %s' % coverage)
            shutil.rmtree(os.path.join('doc', 'coverage'))
        if os.path.exists(generated):
            print('rm -r %s' % generated)
            shutil.rmtree(generated)
        if os.path.exists('MANIFEST'):
            print('rm MANIFEST')
            os.remove('MANIFEST')

class build_doc(Command):
    description = "Build HTML documentation"
    user_options = [
        ('target=', 't', 'What distribution to build for'),
    ]

    def initialize_options(self):
        version = get_version()
        os.environ['SPHINXOPTS'] = '-D release=%s -D version=%s' \
            % (version, version)

        self.target = None

    def finalize_options(self):
        if self.target:
            os.environ['SPHINXOPTS'] += ' -t %s' % self.target
        else:
            os.environ['SPHINXOPTS'] += ' -t source'

    def run(self):
        cmd = ['make', '-C', 'doc', 'html']
        p = Popen(cmd)
        p.communicate()

def get_version():
    """
    Dynamically get the current version.
    """
    version = LATEST_RELEASE  # default
    if os.path.exists('.version'):  # get from file
        version = open('.version').readlines()[0]
    elif os.path.exists('.git'):  # get from git
        cmd = ['git', 'describe', 'master']
        p = Popen(cmd, stdout=PIPE)
        version = p.communicate()[0].decode('utf-8')
    elif os.path.exists('debian/changelog'):  # building .deb
        f = open('debian/changelog')
        version = re.search('\((.*)\)', f.readline()).group(1)
        f.close()

        if ':' in version:  # strip epoch:
            version = version.split(':', 1)[1]
        version = version.rsplit('-', 1)[0]  # strip debian revision
    return version.strip()

class version(Command):
    description = "Output version of this software."
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(get_version())

setup(
    name='DjangoRestAuth',
    version=str(get_version()),
    description='Django RestAuth plugin',
    author='Mathias Ertl',
    author_email='mati@restauth.net',
    url='https://django.restauth.net',
    download_url='https://django.restauth.net/download',
    install_requires=requires,
    license="GNU General Public License (GPL) v3",
    packages=[
        'DjangoRestAuth',
    ],
    data_files=[
        ('share/doc/restauth', ['AUTHORS', 'COPYING', 'COPYRIGHT', ]),
    ],
    cmdclass={
        'build_doc': build_doc,
        'clean': clean,
        'version': version,
    },
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Other Environment",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration :: Authentication/Directory",
    ],
    long_description="""DjangoRestAuth is a Django plugin for RestAuth, a
simple and fast authentication, authorization and user preferences framework.

This project requires `RestAuthClient <https://client.restauth.net>`_
(`PyPI <https://pypi.python.org/pypi/RestAuthClient/>`_) and Django 1.5 or
later."""
)
