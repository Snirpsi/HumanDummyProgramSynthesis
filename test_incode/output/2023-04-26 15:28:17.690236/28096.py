#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers or adds words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <file> [<file>]" % sys.argv[0])
        exit(1)
    
    file = sys.argv[1]
    
    if file:
        remove(file)
    else:
        add(sys.argv[2:])
    
