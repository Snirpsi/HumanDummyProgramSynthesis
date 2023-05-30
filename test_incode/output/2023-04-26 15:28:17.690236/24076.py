#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports or opens a list of numbers. """    
    ports = range(10000, 20000)
    ports_open = []
    for port in ports:
        ports_open.append(port)
    
    while True:
        for port in ports_open:
            