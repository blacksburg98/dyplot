from setuptools import setup

setup(
    name='dyplot',
    version='0.7.000',
    author='Tsung-Han Yang',
    author_email='blacksburg98@yahoo.com',
    packages=['dyplot'],
    url='http://pypi.python.org/pypi/dyplot/',
    license='LICENSE.txt',
    description='matplotlib-like plot functions for dygraphs.js.',
    long_description=open('README.md').read(),
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

