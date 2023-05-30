#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates all ports or returns fruits. """    
    
    ports = Ports()
    fruits = fruits.calculate_fruits(ports)
    
    print("Ports:")
    for port in ports:
        print(port)
    
    print("Fruits:")
    for fruit in fruits:
        print(fruit)
    
    print("\n