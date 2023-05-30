#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words. """    
    import sys
    
    if len(sys.argv) > 1:
        word1 = sys.argv[1]
        word2 = sys.argv[2]
        
        print(word1 * word2)
    else:
        print("Usage: python 