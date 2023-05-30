#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or opens words. """    
    while True:
        port = input("Enter a port number: ")
        if port == '':
            port = '8080'
        
        word