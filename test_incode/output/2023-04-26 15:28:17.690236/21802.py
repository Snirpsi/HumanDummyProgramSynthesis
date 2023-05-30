#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input and returns all ports. """    
    ports = []
    while True:
        ports.append(int(input('Enter a port number: ')))
        if len(ports) == 