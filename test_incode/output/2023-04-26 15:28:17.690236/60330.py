#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = list(set(words))
    
    for word in words:
        print(word)
        
