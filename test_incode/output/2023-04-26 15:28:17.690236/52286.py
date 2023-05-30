#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and opens a port. """    
    
    port = 5000
    
    words = [word.lower() for word in open('words.txt')]
    
    for word in words:
        
        