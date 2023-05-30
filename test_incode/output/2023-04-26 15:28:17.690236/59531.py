#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits and prints all ports. """    
    ports = range(5000)
    fruits = []
    for port in ports:
        fruits.append(