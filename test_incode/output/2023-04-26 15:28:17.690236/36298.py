#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores all ports and converts numbers. """    
    ports = ports_generator()
    ports_converted = ports_converter(ports)
    ports_converted.to_csv("ports.csv")
    
