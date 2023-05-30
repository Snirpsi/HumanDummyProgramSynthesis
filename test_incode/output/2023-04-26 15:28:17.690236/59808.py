#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores user input or prints a list of words. """    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: python wordlist.py [wordlist.txt]")
    else:
        with open(sys.argv[1]) as f:
            words = f.read().splitlines()
        
        print(words)
    
