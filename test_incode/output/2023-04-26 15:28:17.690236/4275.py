#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input. """    
    while True:
        command = input("Enter a command: ")
        if command == "exit":
            break
        elif command == "help":
            print("Commands:")
            print("  exit: exit the program")
            print("  help: display this help message")
        else:
            print("Invalid command")

<|/ file ext=.py |>