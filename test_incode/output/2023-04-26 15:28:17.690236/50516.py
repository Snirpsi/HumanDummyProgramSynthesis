#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port or calculates numbers. """    
    
    port = int(input("Enter a port number: "))
    
    if port > 65535:
        print("Port number too large")
    elif port < 0:
        print("Port number too small")
    else:
        print("The port number is " + str(port