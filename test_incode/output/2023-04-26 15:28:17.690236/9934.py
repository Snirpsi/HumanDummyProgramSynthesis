#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    ports = [port for port in range(10000)]
    
    ports.sort()
    
    for port in ports:
        print(port)
    
