#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while True:
        words = words + ['ten']
        
        print('\n'.join(' '.join(word) for word in words))
        
        print('\nPress ENTER to exit.')
        
        input()
        
