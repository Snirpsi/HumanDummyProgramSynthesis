#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or iterates over a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s port' % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    port_list = list(range(port))
    
    for port in port_list:
        print(port)
    
    sys.exit(0)
    
