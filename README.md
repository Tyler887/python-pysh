# PySH
PySH, a PowerShell-like shell built on Python.

Similar to PWSH, PySH has better type syntax than PowerShell. It's more easier to understand PySH than PWSH.

PySH is work in progress. I would enjoy it if you would add more commands, fix bugs, etc.

**I do not offer any warranty for PySH. Use it at your own risk.**
## Run
### Interpreter
[Download PySH](https://github.com/tyler887/python-pysh/releases) if you havent and open the `shell.py`.
### IDLE
Download PySH if you havent, open the IDLE Shell, open the `shell.py`, and run it.

Note that some commands like `cls` will not work since unlike using the interpreter, they open in the system terminal (Windows 11 terminal or something like that) and not the IDLE Shell.
## Q&A
### Is PySH free for commercial use? In addition, can I make modified versions?
For both, yes. PyShell is completely free of charge, and you are welcome to modify it or commercially use it. PySH is considered free, which requires these rights. You do not need permission in order to redistribute PySH - just download it!

**Warning for all users - PLEASE READ** ([⚓ copyright-warning](#copyright-warning))<br />
<a name="copyright-warning"></a>
"Completely free of charge" must not be confused with "completely free". Python PySH is copyrighted software, *not* public domain software. There are some restrictions on redistribution and use, see the [`LICENSE` file](LICENSE).
### What can I do?
You can run `commands` to see the list of commands. If you cannot understand the list, try `print Hello world!` for the old-school Hello World in the shell.
### What is the minimum Python version required for PySH?
You need Python 3.9 or any later version to use PySH, as specified in the Pipfile.
### Why does PySH have to download dependencies from PyPI that I already installed?
PySH uses features in Python not bundled with Python. It must download dependencies in order to download them. If you have an older version, you must read the `shell.py`, copy the dependency functions, import the OS module, and run those dependency functions with an addition of the `--upgrade` option to update all dependencies.
### When will this be ported to Go? It's faster than Python.
Maybe after I know how I create a standalone "CLI" in Go. I know Golang is faster than Python, according to a Stack Overflow post. It says, "Go is the way to Go", and I think the post was "true". I saw `gh` which ran faster than `pysh`, LOL ;)
