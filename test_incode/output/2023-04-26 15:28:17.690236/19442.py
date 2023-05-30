#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input or opens a port. """    
    while True:
        port = int(input("Port: "))
        if port == -1:
            break
        
        