print("Pyshell  Copyright (C) 2022  Tyler887 Github")
print("This program comes with ABSOLUTELY NO WARRANTY.")
print("This is free software, and you are welcome to redistribute it")
print("under certain conditions.")
print("")
import os
import pip
import platform
import signal
import time
from colorama import init
init()
 

while True:
  cd = os.getcwd()
  command = input("PYSH " + cd + " > ")
  if command == "print" or command == "print ":
    print("pysh aborted as it found a bug in your command!\nbug: cannot use only `print', must set input for operation")
  elif command == "exit":
    exitconf = input("Are you sure you want to exit PyShell? (y/n)\nanswer: ")
    if exitconf == "y":
      exit(0)
  elif command == "commands":
     print("Commands: print, commands, exit\nTo add more commands, submit a pull request at https://github.com/Tyler887/python-pysh.")
  elif not command.startswith("print "):
    print(Fore.RED + "Command not found or misused. Run `commands' for a list of commands.\nHINT: This error counts as a bug. If you tried to use\necho, you should change it to print.")
    print(Style.RESET_ALL)
  if command.startswith("print "):
    echo = command.replace('print ', '', 1)
    print(echo)
  
