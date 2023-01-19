from setuptools import setup, find_packages
import codecs
import os
from pathlib import Path
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

VERSION = '1.1.4'

# Setting up
setup(
    name="pyvaloapi",
    version=VERSION,
    author="Mohamed Yassine Ahmed Ali",
    author_email="<yassineahmedali02@gmail.com>",
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
