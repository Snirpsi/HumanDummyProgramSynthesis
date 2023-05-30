#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port and enumerates words. """    
    
    port = input('Enter a port number: ')
    
    words = []
    
    while True:
        words.append(port)
        
        port = input('Enter another port number: ')
        
        if port == 'q':
            break
        
    print('\n'.join(words))
    
