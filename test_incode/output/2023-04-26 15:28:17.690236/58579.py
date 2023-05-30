#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port or returns user input. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    