#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words or stores all ports. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = sys.argv[1:]
    
    for word in words:
        print(word)
        
