import os
from setuptools import setup, find_packages

with open("readme.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

NAME = 'w'
VERSION = '0.0.0'

setup(
    name=NAME,
    version=VERSION,
    description='alias commands for windows cmd with prefix w',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=[f'{NAME}.{p}' for p in find_packages(where=NAME)] + [NAME],
    install_requires=[
        'click',
        'pyautogui',
    ],
    python_requires='>=3.',
    author="Jordan Miller",
    author_email="iamajordanmiller@gmail.com",
    url="https://bitbucket.wcf.com/wcf",
    entry_points={"console_scripts": ["w = w.cli.w:main"]})
