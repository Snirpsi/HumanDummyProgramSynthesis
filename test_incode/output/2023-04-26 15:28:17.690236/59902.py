#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or stores a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 wordlist.py <words>")
        sys.exit()
    
    words = sys.argv[1:]
    
    wordlist = list(set(words))
    
    for word in wordlist:
        print(word)
    
