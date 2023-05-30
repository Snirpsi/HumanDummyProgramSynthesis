#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words or enumerates user input. """    
    
    import sys
    
    words = sys.argv[1:]
    
    if words:
        words = words.split()
        
        for word in words:
            print(word)
    else:
        print("Usage: python addwordlist.py word1 word2 word3 ...")
        
