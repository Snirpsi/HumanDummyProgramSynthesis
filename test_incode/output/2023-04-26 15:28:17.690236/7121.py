#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a port or removes user input. """    
    
    port = int(input("Enter a port number: "))
    
    if port == -1:
        print("No port number given.")
    else:
        print("Port number 