from distutils.core import setup # Need this to handle modules
os.system('python3 -m pip install art')
import py2exe 
import os
import pip
from art import *
import platform
setup(console=['./shell.py']) # Calls setup function to indicate that we're dealing with a single console application
