#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port. """    
    port = '/dev/ttyACM0'
    ports = enumeratePort(port)
    for p in ports:
        print(p)
    
