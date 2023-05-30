#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    import sys
    
    ports = []
    
    for port in sys.argv[1:]:
        ports.append(port)
    
    ports.sort()
    
    print('\n'.join(ports))
    
