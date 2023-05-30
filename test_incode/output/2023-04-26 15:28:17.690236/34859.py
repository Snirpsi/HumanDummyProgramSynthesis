#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or returns all ports. """    
    while True:
        ports = input('Enter ports separated by commas:')
        ports = ports.split(',')
        ports = [int(p) for p in ports]
        print(ports)
        
