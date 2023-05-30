#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port or stores a port. """    
    port = None
    
    try:
        port = int(input("Enter a port number: "))
    except:
        print("Invalid port number")
        
    if port is not None:
        print("The port number is ", port)
    else:
        print("The port number is not set")
        
