#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words or iterates over words. """    
    
    words = []
    
    while True:
        words.append(input('Enter a word: ').strip())
        
        if words:
            print(*words, sep='