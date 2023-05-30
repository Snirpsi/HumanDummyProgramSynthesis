#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports and returns fruits. """    
    ports = range(8000, 8100)
    fruits = []
    for port in ports:
        fruits.append(