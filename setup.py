from distutils.core import setup
import py2exe

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.version = "1.0.0.0"
        self.company_name = "Tyler Eight-Eight-Seven"
        self.copyright = "Copyright (c) 2022 Tyler887, All Rights Reserved"
        self.name = "My Program"

target = Target(
    description = "The PyShell project is an open source project to make advanced users more productive.",
    script = "Main.py",
    dest_base = "PyShell")
setup(
    options = {'py2exe': {'bundle_files': 1,
                          'compressed': True}},
    zipfile = None,
    console = [target]
)
