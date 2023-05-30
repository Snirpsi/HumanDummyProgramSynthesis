#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    words_to_remove = sys.argv[1]
    
    words = words_to_remove.split(' ')
    
    words = [word for word in words if word not in 