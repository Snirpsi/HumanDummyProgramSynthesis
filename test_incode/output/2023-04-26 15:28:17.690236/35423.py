#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports or opens user input. """    
    while True:
        port = int(input("Enter a port: "))
        if port == -1:
            break
        
        