#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and converts words. """    
    while True:
        port = int(input('Enter a port number: '))
        word = str(input('Enter a word: '))
        
        port.append(word)
        
        