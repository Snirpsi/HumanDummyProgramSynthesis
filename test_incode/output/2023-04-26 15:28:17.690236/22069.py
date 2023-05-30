#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port or calculates numbers. """    
    
    port = '/dev/ttyUSB0'
    
    ports = [port]
    
    ports_numbers = []
    
    while True:
        ports_numbers.append(