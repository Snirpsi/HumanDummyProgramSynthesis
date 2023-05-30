#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port and prints all ports. """    
    
    ports = range(1,65535)
    
    while True:
        for port in ports:
            print('Port {}: {}'.format(port, port*