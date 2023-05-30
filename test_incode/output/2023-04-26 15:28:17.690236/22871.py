#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports or multiplyes fruits. """    
    while True:
        ports = list(fruits.keys())
        fruits.clear()
        for port in ports:
            fruits[port] = fruits[port] * 2
        fruits.