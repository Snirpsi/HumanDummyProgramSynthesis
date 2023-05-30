#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over fruits and converts fruits. """    
    fruits = ['apple', 'orange', 'banana', 'kiwi']
    fruits_converted = []
    for fruit in fruits:
        fruits_converted.append(fruit.replace('_', ' '))
    print('Converted fruits: ' + ', '.join(fruits_converted))
    
