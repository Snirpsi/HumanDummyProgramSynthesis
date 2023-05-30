#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port. """    
    import sys
    port = int(sys.argv[1])
    
    ports = [
        (port, port),
        (port + 1, port + 1),
        (port + 2, port + 2),
        (port + 3, port + 3),
    ]
    
    for port, next_port in ports:
        print('port {}: {}'.format(port, next_port))
    
