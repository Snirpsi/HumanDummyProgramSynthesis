#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes fruits. """    
    
    fruits = ['apple', 'banana', 'orange', 'kiwi', 'grape', 'pear']
    
    for fruit in fruits:
        if fruit == 'apple':
            fruits.remove('apple')
            
    for fruit in fruits:
        print('{} is now {}'.format(fruit, fruit