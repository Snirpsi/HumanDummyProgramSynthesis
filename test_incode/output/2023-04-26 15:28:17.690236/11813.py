#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words. """    
    import sys
    
    word1 = sys.argv[1]
    word2 = sys.argv[2]
    
    word1 = word1.lower()
    word2 = word2.lower()
    
    word1 = word1.split()
    word2 = word2.split()
    
    word1