#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports and returns fruits. """    
    
    ports = Ports()
    fruits = ports.get_fruits()
    
    for fruit in fruits:
        print(fruit)
    
