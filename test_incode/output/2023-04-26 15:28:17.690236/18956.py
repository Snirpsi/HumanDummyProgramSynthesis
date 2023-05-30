#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers and converts words. """    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg.strip().lower())
    
    for word in words:
        print(word)
        
