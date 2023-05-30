#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port. """    
    import sys
    port = int(sys.argv[1])
    
    ports = [port for port in range(65536)]
    
    ports.sort()
    
    print('\n'.join(map(str, ports)))
    
