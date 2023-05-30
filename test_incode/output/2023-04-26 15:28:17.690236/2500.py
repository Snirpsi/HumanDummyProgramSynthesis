#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and converts a list of numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    ports.sort()
    
    ports_open = []
    for port in ports:
        ports_open.append(port)
        
    ports_open = sorted(ports_open)
    
    ports_open = ports_open[::-1]
    
    ports_open = ports_open[: