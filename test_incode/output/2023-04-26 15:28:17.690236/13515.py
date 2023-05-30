#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or opens words. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        if arg == '--ports':
            ports = ports + list(range(8000, 8999))
        else:
            ports.append(int(arg))
    
    ports.sort()
    
    for port in ports:
        