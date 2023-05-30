#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or converts a list of words. """    
    
    ports = sys.argv[1]
    
    if ports == 'all':
        ports = range(8000, 8100)
    
    ports = list(map(int, ports.split(',')))
    
    words = []
    
    for port in ports:
        words += ['