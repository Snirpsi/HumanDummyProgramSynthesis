#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input and converts words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python word.py <word>")
        exit(1)
    
    word = sys.argv[1]
    
    print(word)
    
    