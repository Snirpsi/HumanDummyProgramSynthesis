#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over fruits and calculates all ports. """    
    fruits = ['apple', 'banana', 'orange', 'kiwi']
    ports = []
    for fruit in fruits:
        ports.append(fruit + ' is ' + fruit + ' ' + fruit)
    print(ports)
    
