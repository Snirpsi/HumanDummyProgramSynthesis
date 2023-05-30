#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers or prints words. """    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        if arg == '--help':
            print(__doc__)
            sys.exit(0)
        else:
            words.append(arg)
    
    for word in words:
        print(word)
        
