#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or returns words. """    
    port = '8080'
    words = []
    while port != '':
        port = input('Enter a port number: ')
        words.append(port)
        print('\n'.join(words))
        
