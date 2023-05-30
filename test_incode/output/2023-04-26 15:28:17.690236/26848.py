#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port and iterates over a list of words. """    
    
    words = ['cat', 'dog', 'mouse']
    
    while True:
        port = input('Enter a port number: ')
        
        if port == 'stop':
            break
        
        print('\n