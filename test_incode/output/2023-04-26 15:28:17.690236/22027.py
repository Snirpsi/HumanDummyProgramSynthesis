#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers or removes all ports. """    
    ports = range(1,65535)
    while True:
        try:
            ports.remove