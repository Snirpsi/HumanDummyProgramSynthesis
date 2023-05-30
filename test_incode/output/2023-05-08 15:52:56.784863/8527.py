#!/usr/bin/python3
if __name__ == '__main__':
    #A program that iterates over user input.
    #It will print out the user's input until the user enters exit.
    import sys
    while(True):
        command = input("Enter a command: ")
        if command == "exit":
            sys.exit()
        else:
            print(command)

