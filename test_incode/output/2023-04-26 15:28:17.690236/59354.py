#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 addwordlist.py wordlist")
        sys.exit()
    
    wordlist = sys.argv[1]
    
    words = wordlist.split()
    
    wordlist.close()
    
    for word in words:
        print("