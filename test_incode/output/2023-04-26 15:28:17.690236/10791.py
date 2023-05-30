#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words and returns a port. """    
    import sys
    wordlist = sys.argv[1:]
    
    port = 0
    for word in wordlist:
        port += 1
        
    print(port)
    
