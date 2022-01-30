print("Pyshell  Copyright (C) 2022  Tyler887 Github")
print("This program comes with ABSOLUTELY NO WARRANTY.")
print("This is free software, and you are welcome to redistribute it")
print("under certain conditions.")
print("")
import os
import pip
import platform
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

while True:
  cd = os.getcwd()
  command = input("PYSH " + cd + " > ")
  if command == "print" or command == "print ":
    print(bcolors.FAIL + "pysh aborted as it found a bug in your command!\nbug: cannot use only `print', must set input for operation" + bcolors.RESET)
  elif command == "exit":
    exitconf = input(bcolors.WARNING + "Are you sure you want to exit PyShell? (y/n)\nanswer: " + bcolors.RESET)
    if exitconf == "y":
      exit(0)
  elif command == "commands":
     print("Commands: print, commands, exit\nTo add more commands, submit a pull request at https://github.com/Tyler887/python-pysh.")
  elif not command.startswith("print "):
    print(bcolors.FAIL + "Command not found or misused. Run `commands' for a list of commands.\nHINT: This error counts as a bug. If you tried to use\necho, you should change it to print." + bcolors.RESET)
    print(Style.RESET_ALL)
  if command.startswith("print "):
    echo = command.replace('print ', '', 1)
    print(echo)
  
