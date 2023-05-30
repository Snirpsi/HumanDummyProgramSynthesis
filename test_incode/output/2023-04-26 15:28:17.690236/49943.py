#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or stores a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1].split()
    
    words = [word.strip() for word in words]
    
    removeWords(words)
    
