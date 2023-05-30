#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers and enumerates a port. """    
    ports = [
        port for port in range(1, 65535)
    ]
    
    while True:
        port