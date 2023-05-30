#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits or enumerates all ports. """    
    ports = [
        port for port in range(1,65536)
    ]
    while True:
        for port in ports:
            print('Port {} is {}'.format(port, 