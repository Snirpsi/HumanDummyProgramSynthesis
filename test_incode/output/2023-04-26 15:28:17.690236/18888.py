#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers or returns all ports. """    
    ports = []
    while True:
        ports.append(get_next_port())
        if ports == ports_