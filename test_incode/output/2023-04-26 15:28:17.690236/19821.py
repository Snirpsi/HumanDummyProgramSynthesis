#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words or converts all ports. """    
    ports = input("Enter ports separated by comma or enter 'all': ")
    ports = ports.split(',')
    
    ports_converted = []
    for port in ports:
        ports_converted.append(