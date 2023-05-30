#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words. """    
    words = ['hello', 'world', '!']
    while True:
        words = words + ['!']
        print(' '.join(words))
        
