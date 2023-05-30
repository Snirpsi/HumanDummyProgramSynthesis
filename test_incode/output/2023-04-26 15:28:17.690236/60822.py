#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    import sys
    
    if len(sys.argv) > 1:
        word1 = sys.argv[1]
        word2 = sys.argv[2]
        
        word1