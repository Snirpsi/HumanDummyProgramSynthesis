#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers or removes words. """    
    while True:
        command = input("Enter a command: ")
        if command == "add":
            add(