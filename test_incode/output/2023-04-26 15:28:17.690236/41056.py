#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a port or adds numbers. """    
    port = int(input("Enter a port number: "))
    
    if port > 65535:
        print("Port number must be less than 65535.")
    else:
        print("Port number has been stored.")
        
