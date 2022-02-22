# PySH: A shell written in Python, tested on CPython
# License: PySH License + GPL-3.0-or-later, see the LICENSE file
#
# Why?
  # PySH was created to correct the buggy
  # Microsoft PowerShell commands and it's
  # incorrect type syntax.
  # It is a free and open source shell,
  # which can also execute commands outside
  # itself.
################# CODE BELOW #############
import os
from os import *
import time
# thanks stack overflow
os.system('cls' if os.name=='nt' else 'clear')


print("Loading PySH 1.1...")
print("------------------------------------------------------------------")
print("Upgrading pip...")
os.system('python3 -m pip install -U pip')
print("------------------------------------------------------------------")
print("Installing dependencies...")
os.system('python3 -m pip install -U art colorama --exists-action s')
print("Import art module")
from art import *
print("Import colorama module")
from colorama import *
print("Launching PySH...")


# thanks stack overflow
os.system('cls' if os.name=='nt' else 'clear')
tprint("PyShell")
print("               version 1.1 // type `update'")
print(Fore.GREEN + "H" + Fore.BLUE + "e" + Fore.CYAN + "l" + Fore.YELLOW + "l" + Fore.RED + "o" + Style.RESET_ALL + "!")
print("type `commands' if you don't know what you can do in this shell")
print("")
errortitle = "ERROR"
warningtitle = "WARNING"
manpagetitle = "MANUAL"
deptitle = "Deprecerated"
import platform
if platform.system() == "Windows":
  os.system('title PyShell 1.1 Beta - ' + os.getcwd())
import tkinter as tk
while True:
  cd = os.getcwd()
  command = input(Back.WHITE + Fore.BLACK + " PYSH " + Style.RESET_ALL + " " + cd + " > ")
  if command == "print" or command == "print ":
    tprint(errortitle)
    print("pysh aborted as it found a bug in your command!\nbug: cannot use only `print', must set input for operation")
  elif command == "exit":
    tprint(warningtitle)
    exitconf = input("Are you sure you want to exit PyShell? (y/n)\nanswer: ")
    if exitconf == "y":
      exit(0)
  elif command == "commands":
     print("Commands: print, commands, exit, cls, version, info\nPlanned: update\nTo add more commands, submit a pull request at https://github.com/Tyler887/python-pysh.\nCommands not bundled can also be executed in PySH (on Windows, WPS is used).")
  elif command == "file":
    tprint(manpagetitle)
    print(Fore.RED + "This command has been removed. Documentation for this command will not be updated." + Style.RESET_ALL)
    print("FILE: open a file in the current directory")
    print("To use this command, use an input value.")
    print("Warning: Python will crash if the file given does not exist.")
  elif command == "info":
    print(Fore.BLUE + "Py" + Fore.GREEN + "Shell " + Style.RESET_ALL + "Version 1.1 (" + Fore.YELLOW + "Beta" + Style.RESET_ALL + ")")
    import sysconfig
    import sys
    print("System name             ", os.name)
    print("Operating system ID     ", sys.platform)
    print("Operating system        ", platform.system())
    print("Platform (sysconfig)    ", sysconfig.get_platform())
    print("Machine                 ", platform.machine())
    print("Architecture            ", platform.architecture())
    print("Python                  ", platform.python_version())
  elif command == "version":
    print("1.1 Open Source")
    print("more info: run `info'")
  elif command == "cls":
    # thanks stack overflow
    os.system('cls' if os.name=='nt' else 'clear')
  elif command == "cd":
    print(os.getcwd())
  elif not command.startswith("print ") and not command.startswith("cd ") and not command.startswith("file "):
    if command != "":
       print(Fore.YELLOW + "Warning: This is an external command or file (not in commands list), and it is not bundled with PyShell.\nPlease only use this command if you trust it. Details at https://tyler887.github.io/python-pysh/why-not-externals" + Style.RESET_ALL)
       if platform.system() == "Windows":
          print("Press any key, if you trust this command...")
          import msvcrt as m
          m.getch()
       if platform.system() == "Windows":
         os.system("powershell -c " + command)
       else:
         os.system(command)


  if command.startswith("cd ") and command != "cd":
    print("This feature is not functional. Sorry...")

  if command.startswith("print ") and command != "print ":
    echo = command.replace('print ', '', 1)
    print(echo)
  if command.startswith("file ") and command != "file":
    print(Fore.RED)
    tprint(deptitle)
    print("This command has been removed because it did not work in any PyShell version." + Style.RESET_ALL)
    print(Fore.BLUE + "Notice: There is another feature similar to the FILE command, external command support.\nConsider using external commands." + Style.RESET_ALL)
  
# End script
