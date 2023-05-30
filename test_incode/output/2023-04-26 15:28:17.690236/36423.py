#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or removes user input. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = []
    
    words = filter(None, words)
    
    for word in words:
        print(word)
        
