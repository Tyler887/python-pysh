import os
print("Installing Nessecary Dependencies...")
os.system('python3 -m pip install art')
from art import * 
# thanks stack overflow
os.system('cls' if os.name=='nt' else 'clear')
tprint("PyShell")
print("Hello!\ntype `commands' if you don't know what you can do in this shell")
print("")
errortitle = "ERROR"
warningtitle = "WARNING"
manpagetitle = "MANUAL"
import platform

while True:
  cd = os.getcwd()
  command = input("PYSH " + cd + " > ")
  if command == "print" or command == "print ":
    tprint(errortitle)
    print("pysh aborted as it found a bug in your command!\nbug: cannot use only `print', must set input for operation")
  elif command == "exit":
    tprint(warningtitle)
    exitconf = input("Are you sure you want to exit PyShell? (y/n)\nanswer: ")
    if exitconf == "y":
      exit(0)
  elif command == "commands":
     print("Commands: print, commands, exit, cls, python-license, version, file\nTo add more commands, submit a pull request at https://github.com/Tyler887/python-pysh.")
  elif command == "python-license":
    license()
  elif command == "file":
    tprint(manpagetitle)
    print("FILE: open a file in the current directory")
    print("To use this command, use an input value.")
    print("Warning: Python will crash if the file given does not exist.")
          
  elif command == "version":
    print("1.0 Open Source")
  elif command == "cls":
    # thanks stack overflow
    os.system('cls' if os.name=='nt' else 'clear')
  elif not command.startswith("print ") and not command.startswith("file "):
    tprint(errortitle)
    print("Command not found or misused. Run `commands' for a list of commands.\nHINT: This error counts as a bug. No commands have aliases and all names are\ncase insensitive.")
  if command.startswith("print "):
    echo = command.replace('print ', '', 1)
    print(echo)
  if command.startswith("file ") and command != "file":
    file = command.replace('file ', '', 1)
    open(file)
  
