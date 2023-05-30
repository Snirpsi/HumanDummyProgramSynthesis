#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or iterates over numbers. """    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = range(10)
    
    for word in words:
        print(word)
        
