import os
from setuptools import setup, find_packages

setup(
    name='dyplot',
    version='0.8.9',
    author='Tsung-Han Yang',
    author_email='blacksburg98@yahoo.com',
    packages=find_packages(),
    url='https://dyplot.readthedocs.org',
    license='LICENSE.txt',
    description='matplotlib-like plot functions for dygraphs.js and c3.js.',
    install_requires=[
        "pandas >= 1.3.4",
    ],
    classifiers = [
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Scientific/Engineering :: Visualization",
        "Programming Language :: JavaScript",
    ],
)

