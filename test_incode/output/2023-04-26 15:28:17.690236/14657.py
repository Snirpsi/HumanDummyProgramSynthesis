#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words or adds all ports. """    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(0)
    
    words = sys.argv[1].split()
    
    removeWords(words)
    addAllPorts(words)
    
