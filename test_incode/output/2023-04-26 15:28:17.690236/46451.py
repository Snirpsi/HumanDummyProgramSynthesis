#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s word1" % sys.argv[0])
        sys.exit()
    
    word1 = sys.argv[1]
    
    word2 = word1.split()
    
    word3 = " ".join(word2)
    
    print(word3)
    
