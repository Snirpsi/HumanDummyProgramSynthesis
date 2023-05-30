#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    words = ['hello', 'world', '!']
    
    while True:
        words = words + ['!']
        
        print(' '.join(words))
        
        if input('Continue? [y/N]').lower() != 'y':
            break
        
    print('Done!')
    
