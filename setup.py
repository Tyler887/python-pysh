import os

try:
  import requests
except ImportError:
  print("Trying to Install required module: requests\n")
  os.system('python -m pip install requests')
# -- above lines try to install requests module if not present
# -- if all went well, import required module again ( for global access)
import requests
setup(console=['./shell.py']) # Calls setup function to indicate that we're dealing with a single console application
