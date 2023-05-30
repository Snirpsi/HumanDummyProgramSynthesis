#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes fruits. """    
    
    fruits = ['apple', 'orange', 'pear', 'banana', 'cherry']
    
    fruits_removed = [x for x in fruits if x not in fruits_removed]
    
    print(fruits_removed)
    
