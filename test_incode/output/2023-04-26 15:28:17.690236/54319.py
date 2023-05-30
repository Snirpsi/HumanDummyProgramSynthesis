#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input or returns a port. """    
    
    port = input("Enter a port: ")
    
    if port == "help":
        print("Enter a port:")
        print("    help: Prints this help message")
        print("    exit: Exits the program")
        
    else:
        return port
    
