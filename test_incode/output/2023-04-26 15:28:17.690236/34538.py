#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input or returns a port. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    if port == '':
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit()
    
    