#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words or converts a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = sys.argv[0]
    
    words = list(filter(None, words.split(' ')))
    
    words.sort()
    
    for word in words:
        print(word)
        
