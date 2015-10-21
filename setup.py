import os
from setuptools import setup, find_packages

__currdir__ = os.getcwd()
__readme__ = os.path.join(__currdir__, 'README.txt')
setup(
    name='dyplot',
    version='0.7.10',
    author='Tsung-Han Yang',
    author_email='blacksburg98@yahoo.com',
    packages=find_packages(),
    url='http://pypi.python.org/pypi/dyplot/',
    license='LICENSE.txt',
    description='matplotlib-like plot functions for dygraphs.js and c3.js.',
    long_description = open(__readme__).read(),
    install_requires=[
        "pandas >= 0.7.3",
    ],
    classifiers = [
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Scientific/Engineering :: Visualization",
        "Programming Language :: JavaScript",
    ],
)

