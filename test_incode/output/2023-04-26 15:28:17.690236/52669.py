#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s word1 word2 ..." % sys.argv[0])
        exit(1)
    
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    
    words.sort()
    
    for word in words:
        print(word*