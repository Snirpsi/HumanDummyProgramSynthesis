#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        sys.stdout.write(word + '\n')
        sys.stdout.flush()
        
