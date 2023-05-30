#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports and converts a list of words. """    
    import sys
    wordlist = sys.argv[1:]
    
    ports = []
    
    for word in wordlist:
        ports.append(word.split(":")[0])
    
    for port in ports:
        