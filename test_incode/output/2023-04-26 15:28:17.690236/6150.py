#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers or converts a list of words. """    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: python list.py <list>")
    else:
        list_to_words(sys.argv[1])
    
