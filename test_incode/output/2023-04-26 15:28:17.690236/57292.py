#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port or adds a list of numbers. """    
    port = '/dev/ttyUSB0'
    ports = [port]
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    
    for port in ports:
        