#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    words = ['hello', 'world', '!']
    
    while True:
        print('\nMultiplying words:')
        for word in words:
            print(word*