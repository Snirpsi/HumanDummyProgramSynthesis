#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports or stores user input. """    
    while True:
        ports = input("Enter ports separated by comma: ").split(',')
        for port in ports:
            