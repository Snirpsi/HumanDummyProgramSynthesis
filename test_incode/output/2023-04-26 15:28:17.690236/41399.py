#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words. """    
    while True:
        words = input('Enter a word: ').split()
        
        if len(words) == 0:
            break
        
        words = [word.lower() for word in words]
        
        print(' '.join(words))
        
