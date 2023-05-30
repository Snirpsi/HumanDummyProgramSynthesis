#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words or adds words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <word1> <word2>" % sys.argv[0])
        sys.exit()
    
    word1 = sys.argv[1]
    word2 = sys.argv[2]
    
    word1 = word1.lower()
    word2 = word2.lower()
    
    word1 = word1.split()
    word2 = word2.split()
    
    word1