from setuptools import setup, find_packages
import codecs
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A cross platform Python package to automate sending and receiving of WhatsApp messages using PyAutoGUI.'

# Setting up
setup(
    name="WhatsAppBot_Nanda",
    version=VERSION,
    author="Nanda Kishore B",
    author_email="<pgsbssnk@gmail.com>",
    url='https://github.com/nandakishfast/WhatsAppBot_Nanda',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pyautogui', 'scipy', 'pyperclip', 'numpy', 'pynput', 'tkvideo', 'Pillow'],
    extras_require={
        'win32': 'pywin32'
    },
    keywords=['WhatsApp', 'WhatsApp Bot', 'Chat Bot', 'automation'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)