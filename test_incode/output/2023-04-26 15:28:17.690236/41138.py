#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers or stores a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['one', 'two', 'three']
    
    for word in words:
        print(word)
    
