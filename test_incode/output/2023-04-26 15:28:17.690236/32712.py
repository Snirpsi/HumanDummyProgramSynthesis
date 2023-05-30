#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of numbers or multiplyes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python wordlist.py <words>")
        exit(1)
    
    words = sys.argv[1:]
    
    for word in words:
        print(word