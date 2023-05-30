#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words and prints words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while True:
        words.remove(words.pop(0))
        print(' '.join(words))
        
