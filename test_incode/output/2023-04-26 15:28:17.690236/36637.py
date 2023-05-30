#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or opens words. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        
        try:
            