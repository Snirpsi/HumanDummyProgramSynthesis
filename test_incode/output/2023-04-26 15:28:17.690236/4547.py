#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds all ports or calculates fruits. """    
    
    ports = Ports()
    fruits = fruits.calculate_fruits(ports)
    
    print('Fruits:')
    for fruit in fruits:
        print(fruit)
    
