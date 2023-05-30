#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words or enumerates a port. """    
    port = int(sys.argv[1])
    
    words = wordlist(port)
    
    for word in words:
        print(word)
    
