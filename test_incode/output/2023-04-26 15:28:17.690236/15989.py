#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers and removes all ports. """    
    ports = range(0,65535)
    ports_removed = []
    for port in ports:
        ports_removed.append(port)
    ports_removed = list(set(ports_removed))
    print(ports_removed)
    
