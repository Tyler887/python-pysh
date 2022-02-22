from distutils.core import setup # Need this to handle modules
import py2exe 
from time, os, colorama, art, sys, sysconfig, platform import * # We have to import all modules used in our program
import msvcrt as m
setup(console=['shell.py']) # Calls setup function to indicate that we're dealing with a single console application
