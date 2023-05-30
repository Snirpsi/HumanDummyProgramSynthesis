#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port and iterates over a list of numbers. """    
    port = '/dev/ttyUSB0'
    
    ports = [int(p) for p in 