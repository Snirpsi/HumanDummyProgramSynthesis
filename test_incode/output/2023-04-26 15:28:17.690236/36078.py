#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words and opens all ports. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 wordlist.py [wordlist]")
        exit()
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split()
    
    wordlist.sort()
    
    ports = openports(wordlist)
    
    for port in ports:
        
        