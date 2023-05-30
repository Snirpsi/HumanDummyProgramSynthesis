#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words or multiplyes words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for word in words:
        print(word