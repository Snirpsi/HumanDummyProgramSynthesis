#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words or returns a port. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: python remove-word.py <words>")
        sys.exit()
    
    words = sys.argv[1:]
    
    removeWords(words)
    
