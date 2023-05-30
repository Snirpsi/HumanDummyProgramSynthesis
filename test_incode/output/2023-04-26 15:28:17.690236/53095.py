#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input or adds all ports. """    
    while True:
        ports = input('Enter ports separated by comma: ')
        ports = ports.split(',')
        for port in ports:
            print(port)
