#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or returns words. """    
    import sys
    words = sys.argv[1:]
    
    if len(words) == 0:
        print("Usage: python words.py")
    else:
        for word in words:
            print(word)
    
