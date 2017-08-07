"""
A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject/blob/master/setup.py

"""
from setuptools import setup, find_packages
from codecs import open # consistent encoding
from os import path

with open('README.md') as f:
    readme = f.read()

setup(name='palm_tree',
      version='0.0.1',
      description='palm tree is good for you',
      url='https://github.com/stevealbertwong/cautious-palm-tree.git',
      author='Lexica',
      author_email='contact@lexica.io',    
      license='MIT',
      packages=['palmtree'])   
