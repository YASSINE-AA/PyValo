from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.8'
DESCRIPTION = 'Unofficial Valorant API for Python'
LONG_DESCRIPTION = 'A Python module that allows you to directly interact with the Valorant Game Client.'

# Setting up
setup(
    name="pyvaloapi",
    version=VERSION,
    author="Mohamed Yassine Ahmed Ali",
    author_email="<yassineahmedali02@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'api', 'valorant', 'games', 'gaming', 'http'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)