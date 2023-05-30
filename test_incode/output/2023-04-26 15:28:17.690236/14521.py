#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words or opens all ports. """    
    ports = sys.argv[1:]
    ports = ports.split(",")
    ports = ports.