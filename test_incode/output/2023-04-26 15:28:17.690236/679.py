#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers and removes a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    ports = [int(port) for port in range(1, 65535)]
    
    ports.remove(port)
    
    print('\n'.join(map(str, ports)))
    
