from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# change this every time you make a new release
VERSION = '0.1.2'
DESCRIPTION = 'the python library that makes PYGAME easier to use'

# Setting up
setup(
    name="easier_pygame",
    version=VERSION,
    author="OortStudios (ShakedKod)",
    author_email="<OortStudiosOfficial@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        "pygame",
        "moviepy"
    ],
    keywords=[
        "python",
        "pygame",
        "easier",
        "easier pygame"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)