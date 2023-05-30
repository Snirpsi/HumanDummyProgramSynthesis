#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input or removes fruits. """    
    fruits = ['apple', 'orange', 'banana', 'grapes', 'watermelon']
    
    for fruit in fruits:
        if fruit == 'apple':
            fruits.remove('apple')
            
    for fruit in fruits:
        print(