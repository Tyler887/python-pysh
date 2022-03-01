from distutils.core import setup
import py2exe

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.version = "1.1"
        self.company_name = "Tyler Eight-Eight-Seven"
        self.copyright = "Copyright (c) 2022 Tyler887, All Rights Reserved"
        self.name = "PyShell"

target = Target(
    description = "PyShell Windows Binary Build",
    script = "shell.py",
    dest_base = "pysh")
setup(
    options = {'py2exe': {'bundle_files': 1,
                          'compressed': True}},
    zipfile = None,
    console = [target]
)
