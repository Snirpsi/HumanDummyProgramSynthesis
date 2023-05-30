#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words or converts a list of words. """    
    
    words = sys.argv[1:]
    
    if len(words) == 0:
        print('Usage: python word