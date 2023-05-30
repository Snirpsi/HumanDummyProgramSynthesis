#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints fruits and removes a list of words. """    
    fruits = ['apple', 'banana', 'orange', 'pear', 'grape', 'mango']
    
    fruits_removed = remove_words(fruits, ['apple', 'pear'])
    print(fruits_removed)
    
