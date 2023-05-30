#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or adds all ports. """    
    while True:
        ports = input("Enter ports separated by comma:\n").split(',')
        for port in ports:
            