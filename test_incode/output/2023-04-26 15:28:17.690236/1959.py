#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg.strip())
    
    words.sort()
    
    for word in words:
        print(word)
        
