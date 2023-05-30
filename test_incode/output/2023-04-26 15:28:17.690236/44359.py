#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        command = input("Enter a command: ")
        if command == "quit":
            break
        elif command == "help":
            print("\nAvailable commands:")
            print("\tquit: quits this program")
            print("\thelp: prints this help")
        else:
            print("Invalid command")
