#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words and iterates over a port. """    
    
    words = []
    
    while True:
        words.append(input('Enter a word: '))
        
        if len(words) == 