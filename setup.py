import os
print("Installing Nessecary Dependencies...")
os.system('python3 -m pip install art')
from art import *
from platform import *
from py2exe import *
setup(console=['./shell.py']) # Calls setup function to indicate that we're dealing with a single console application
