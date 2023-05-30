#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and returns all ports. """    
    while True:
        ports = input("Enter ports separated by commas (no spaces):")
        ports = ports.split(',')
        for port in ports:
            print(port)
