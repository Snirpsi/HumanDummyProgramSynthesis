#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port or multiplyes a port. """    
    port = int(input("Enter a port (1-65535): "))
    
    if port > 65535:
        print("Error: port number too large")
    else:
        port = port * 2
        
        print("The port number is", port)
    
