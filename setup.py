from distutils.core import setup
import py2exe

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console = [{'script': "shell.py"}],
    zipfile = None,
    dest_base = "PyShell for Windows",
)
