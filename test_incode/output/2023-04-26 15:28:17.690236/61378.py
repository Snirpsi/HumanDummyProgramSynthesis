#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds numbers or adds a port. """    
    
    port = int(input("Enter a port number: "))
    
    if port > 65535:
        print("Port number must be between 1 and 65535")
    elif port < 1:
        print("Port number must be between 1 and 65535")
    else:
        print("The port number is", port)
    
