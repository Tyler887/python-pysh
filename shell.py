print("PyShell v1.0 - Open Source")
print("")
import os
import pip
import platform


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
     print("Commands: print, commands, exit, python-license, version\nTo add more commands, submit a pull request at https://github.com/Tyler887/python-pysh.")
  elif command == "python-license":
    license()
  elif command == "version":
    print("1.0 Open Source")
  elif not command.startswith("print "):
    print("Command not found or misused. Run `commands' for a list of commands.\nHINT: This error counts as a bug. No commands\nhave aliases.")
  if command.startswith("print "):
    echo = command.replace('print ', '', 1)
    print(echo)
  
