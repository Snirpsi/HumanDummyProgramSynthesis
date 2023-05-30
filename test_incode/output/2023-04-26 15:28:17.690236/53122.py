#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    import sys
    
    ports = []
    
    for port in range(1024):
        ports.append(port)
    
    ports.sort()
    
    sys.stdout.write('\n'.join(map(str, ports)))
    
    sys.stdout.flush()
    
    