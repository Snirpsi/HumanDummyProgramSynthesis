#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports or enumerates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = range(1024)
    
    for port in ports:
        print(port)
        
