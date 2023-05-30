#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port and multiplyes user input. """    
    while True:
        port = input('Enter a port number: ')
        port = int(port)
        
        multiplier = 1
        
        while(multiplier < port):
            multiplier = multiplier * 