#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports or enumerates a list of numbers. """    
    ports = range(1,65535)
    while True:
        for port in ports:
            print('Port {} is open at {}'.format(port,