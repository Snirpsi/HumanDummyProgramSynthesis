#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits and calculates numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_numbers = []
    
    for fruit in fruits:
        fruits_numbers.append(len(fruit))
        
    print('Fruits: ', fruits)
    print('Fruit numbers: ', fruits_numbers)
    
