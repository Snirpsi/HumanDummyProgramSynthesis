#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or converts words. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    words.sort()
    
    for word in words:
        print(word)
    
