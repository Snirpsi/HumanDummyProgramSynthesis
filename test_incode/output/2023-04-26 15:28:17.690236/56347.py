#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or enumerates numbers. """    
    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        if arg == '-':
            words.extend(sys.argv[2:])
        else:
            words.append(arg)
    
    if len(words) == 0:
        print('Usage: python -m word