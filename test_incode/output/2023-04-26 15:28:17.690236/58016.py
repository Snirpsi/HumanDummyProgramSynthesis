#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input. """    
    while True:
        print("Type 'quit' to quit")
        command = input("Command: ")
        if command == "quit":
            break
        else:
            print(command)
            
