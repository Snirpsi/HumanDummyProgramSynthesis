#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words or converts words. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    words.extend(sys.argv[1:])
    
    words = list(set(words))
    
    if len(words) == 0:
        print("Usage: %s <words>" % sys.argv[0])
        
    for word in words:
        print(word)
        
    
