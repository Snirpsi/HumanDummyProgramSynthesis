#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints fruits and converts words. """    
    fruits = ['apple', 'banana', 'orange', 'pear', 'grape', 'mango']
    fruits_converted = [fruit.lower() for fruit in fruits]
    print('fruits:', fruits)
    print('fruits_converted:', fruits_converted)
    print('fruits_converted:', fruits_converted.