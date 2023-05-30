#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports or converts numbers. """    
    while True:
        ports = [int(port) for port in input().split()]
        for port in ports:
            print(port)
