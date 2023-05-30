#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words or iterates over a port. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        
        port = int(input('Enter a port: '))
        
        port