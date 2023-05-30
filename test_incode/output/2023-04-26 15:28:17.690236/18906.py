#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports and opens user input. """    
    
    while True:
        port = input("Enter a port number: ")
        
        if port == '':
            continue
        
        