#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python calculate_port.py <port>")
        exit(1)
    
    port = sys.argv[1]
    
    print("Calculating port %s" % port)
    
    