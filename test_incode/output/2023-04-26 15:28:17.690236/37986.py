#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words or opens a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = []
    
    multiplied = []
    
    for word in words:
        multiplied.append(word*2)
    
    print(' '.join(multiplied))
    
