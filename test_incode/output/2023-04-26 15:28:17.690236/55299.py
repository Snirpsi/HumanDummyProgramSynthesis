#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports or stores user input. """    
    while True:
        port = int(input('Enter a port number: '))
        if port == -1:
            break
        
        