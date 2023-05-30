#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    import sys
    
    wordlist = sys.argv[1]
    
    words = wordlist.split()
    
    words = [word for word in words if word not in words]
    
    print(" ".join(words))
    
