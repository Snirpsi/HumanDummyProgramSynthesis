#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    fruits_sorted = sorted(fruits, key = len)
    
    fruits_sorted.reverse()
    
    fruits_sorted.append('banana')
    
    fruits_sorted.append('banan