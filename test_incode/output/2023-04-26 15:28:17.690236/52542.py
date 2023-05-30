#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers and converts a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    numbers = map(int, words)
    
    words = [str(n) for n in numbers]
    
    print(" ".join(words))
    
