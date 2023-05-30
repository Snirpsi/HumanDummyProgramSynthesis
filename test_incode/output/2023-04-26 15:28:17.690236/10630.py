#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    import sys
    
    ports = []
    
    for port in range(1, 65535):
        ports.append(port)
    
    ports.sort()
    
    sys.stdout.write('\nPorts: ')
    for port in ports:
        sys.stdout.write(' ' + str(port) + '\n')
    
    sys.stdout.write('\nPress Ctrl-C to exit\n')
    
    sys.stdout.flush()
    
    