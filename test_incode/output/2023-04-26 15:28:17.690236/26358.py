#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words|numbers>" % sys.argv[0])
        sys.exit()
    
    words = 0
    numbers = 0
    
    for arg in sys.argv[1:]:
        if arg == 'words':
            words = 1
        elif arg == 'numbers':
            numbers = 1
        else:
            print("Usage: %s <words|numbers>" % sys.argv[0])
            sys.exit()
    
    if words == 1:
        word