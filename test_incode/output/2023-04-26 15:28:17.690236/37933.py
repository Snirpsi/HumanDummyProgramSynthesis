#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports. """    
    ports = range(65535)
    while True:
        for port in ports:
            print(port)
        ports = range(65535)
