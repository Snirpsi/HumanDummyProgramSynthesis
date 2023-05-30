#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and iterates over all ports. """    
    while True:
        ports = input('Enter ports (separated by commas): ')
        ports = ports.split(',')
        for port in ports:
            print(port)
