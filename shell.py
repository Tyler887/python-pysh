print("Pyshell  Copyright (C) 2022  Tyler887 Github")
print("This program comes with ABSOLUTELY NO WARRANTY.")
print("This is free software, and you are welcome to redistribute it")
print("under certain conditions.")
print("")
import os
import pip
import platform
while True:
  cd = os.getcwd()
  command = input(cd + "> ")
  if command == "print" or command == "print ":
    print("pysh aborted as it found a bug in your command!\nbug: cannot use only `print', must set input for operation")
  if command.startswith("print "):
    echo = command.replace('print ', '', 1)
    print(echo)
