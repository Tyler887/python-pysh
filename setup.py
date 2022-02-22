from distutils.core import setup # Need this to handle modules
import py2exe 
from time import *
from os import *
from colorama import *
from art import *
from sys import *
from sysconfig import *
from platform import *
import msvcrt as m
setup(console=['shell.py']) # Calls setup function to indicate that we're dealing with a single console application
