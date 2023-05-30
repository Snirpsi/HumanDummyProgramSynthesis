#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers and iterates over fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_length = len(fruits)
    fruits_index = 0
    fruits_value = 0
    fruits_sum = 0
    fruits_count = 0
    
    while fruits_index < fruits_length:
        fruits_index = fruits_index + 1
        fruits_value = fruits_value + fruits[fruits_index]
        fruits_sum = fruits_sum + fruits_value
        fruits_count = fruits_count + 1
    
    print('The sum of all fruits: ', fruits_sum)
    print('The total number of fruits: ', fruits_count)
    
