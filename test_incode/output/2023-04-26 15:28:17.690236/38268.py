#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words or adds all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = words.split()
    
    words = [w for w in words if w not in ['-', '?', '!']]
    
    words = list(set(words))
    
    words.sort()
    
    print("\n".join(words))
    
