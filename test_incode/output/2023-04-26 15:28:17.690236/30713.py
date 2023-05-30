#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and opens a port. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    with open('words.txt', 'r') as words:
        words = words.read().splitlines()
    
    words.sort()
    
    open