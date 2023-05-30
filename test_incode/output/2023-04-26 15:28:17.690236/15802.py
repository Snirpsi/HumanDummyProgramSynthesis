#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports or enumerates a list of numbers. """    
    import sys
    
    ports = []
    
    if len(sys.argv) > 1:
        ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        print('Port %d' % port)
    
    if len(ports) == 1:
        print('Port %d' % ports[0])
    
    if len(ports) > 1:
        print('Port %d (%d ports)' % (ports[0], len(ports)))
    
