#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers and stores a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python ports.py <port>")
        sys.exit()
    
    port = int(sys.argv[1])
    
    ports = [port]
    
    for i in range(2, 