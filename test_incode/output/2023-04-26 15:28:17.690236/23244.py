#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words or stores a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: enumerate.py <words>')
        exit()
    
    words = sys.argv[1:]
    
    words = words.split()
    
    for word in words:
        print(word)
        
