#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(-1)
    
    words = sys.argv[1:]
    
    words = list(map(str.strip, words))
    
    words.sort()
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word != '']
    
    words = [word for word in words if word != ' ']
    
    words = [word for word in words if word != '