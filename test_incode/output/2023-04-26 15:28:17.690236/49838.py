#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input or converts a port. """    
    while True:
        port = int(input("Enter a port to convert (1-65535): "))
        if port > 65535:
            print("Port must be between 1 and 65535.")
        elif port < 1:
            print("Port must be between 1 and 65535.")
        else:
            break
    
    
<|/ file source=github ext=.py filename=