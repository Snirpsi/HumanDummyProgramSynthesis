#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or prints words. """    
    ports = range(10000, 65535)
    for port in ports:
        print(port)
