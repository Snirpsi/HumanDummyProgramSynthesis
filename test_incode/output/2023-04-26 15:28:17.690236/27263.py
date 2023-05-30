#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or stores all ports. """    
    while True:
        port = input("Enter a port number: ")
        if port == '':
            break
        
        port = int(port)
        
        