#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers and enumerates fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    fruits_count = collections.Counter(fruits)
    
    for fruit, count in fruits_count.items():
        print('{}: {}'.format(fruit, count))
    
    print('\n\n')
    
    fruits_count = collections.Counter(fruits, 