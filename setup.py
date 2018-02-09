#!/usr/bin/env python
import os
from setuptools import setup, find_packages

PACKAGE_DIR = 'fcc_complaints'

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

with open(os.path.join(os.path.dirname(__file__), PACKAGE_DIR, 'VERSION')) as version:
    VERSION = version.read().strip()


setup(name=PACKAGE_DIR,
      version=VERSION,
      description='FCC Complaint Data API Wrapper',
      long_description=README,
      author='Greg Doermann',
      author_email='gdoermann@cronosa.com',
      url='https://github.com/gdoermann/fcc_complaints',
      packages=find_packages('src/'),
      include_package_data=True,
      install_requires=required
      )
