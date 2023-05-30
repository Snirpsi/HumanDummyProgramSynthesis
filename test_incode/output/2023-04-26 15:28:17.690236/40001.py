#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = sys.argv[0]
    
    words = words.split()
    
    for word in words:
        print(word, end=' ')
        
