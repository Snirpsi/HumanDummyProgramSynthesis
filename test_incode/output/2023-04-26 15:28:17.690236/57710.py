#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words_to_remove" % sys.argv[0])
        exit(1)
    
    words_to_remove = sys.argv[1:]
    
    remove