#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or opens all ports. """    
    ports = range(10000)
    while True:
        for port in ports:
            print('Starting port 