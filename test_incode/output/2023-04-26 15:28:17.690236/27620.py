#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    
    # Print all fruits 
    for fruit in fruits:
        print(fruit)
    
    # Print all fruits with their count
    for fruit in fruits:
        print(fruit, fruits.count(fruit))
    
    # Print all fruits with their count and their name
    for fruit, count in fruits.