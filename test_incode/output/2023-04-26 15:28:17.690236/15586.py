#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words or multiplyes a list of words. """    
    words = ['hello', 'world', '!']
    
    while True:
        
        for word in words:
            print(word)
        
        words = ['hello', 'world', '!']
        
        print('\nPress enter to exit.')
        
        