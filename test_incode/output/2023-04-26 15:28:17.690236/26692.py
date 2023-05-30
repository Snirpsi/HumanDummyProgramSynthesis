#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port or adds numbers. """    
    
    port = int(input("Enter a port number: "))
    
    if port > 65535:
        print("Port number too large")
    elif port < 1:
        print("Port number too small")
    else:
        print("Port number: " + str(port))
    
