#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports or enumerates numbers. """    
    ports = range(1,65535)
    for port in ports:
        print('Port {} is open on {}'.format(port, 