#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words and prints fruits. """    
    words = ['apple', 'banana', 'cherry']
    fruits = ['apple', 'banana', 'cherry']
    
    fruits_multiplied = fruits * words
    
    for fruit in fruits_multiplied:
        print(fruit)
        
