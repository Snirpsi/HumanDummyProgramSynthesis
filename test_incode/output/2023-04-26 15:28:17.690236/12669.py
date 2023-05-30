#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input or returns user input. """    
    while True:
        command = input("Enter a command: ")
        if command == "exit":
            break
        elif command == "help":
            print("Commands:")
            print("  exit: Exit the program")
            print("  help: Print this message")
        else:
            print("Invalid command")
