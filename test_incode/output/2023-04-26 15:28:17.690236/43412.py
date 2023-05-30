#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input and stores a port. """    
    
    port = 1
    
    while True:
        port = input("Enter a port number: ")
        if port == "exit":
            break
        else:
            port = 