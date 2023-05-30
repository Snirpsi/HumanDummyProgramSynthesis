#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers or multiplyes a list of words. """    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: python wordlist.py <wordlist>")
        sys.exit()
    
    wordlist = sys.argv[1]
    
    for word in wordlist.split():
        print(word