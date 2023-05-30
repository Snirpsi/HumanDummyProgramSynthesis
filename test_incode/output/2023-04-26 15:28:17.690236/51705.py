#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports and calculates fruits. """    
    
    ports = range(80, 901)
    fruits = []
    for port in ports:
        fruits.append(