#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input or opens all ports. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        
        port = int(port)
        
        