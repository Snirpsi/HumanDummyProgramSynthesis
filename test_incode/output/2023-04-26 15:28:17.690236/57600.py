#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    for fruit in fruits:
        if fruit == 'cherry':
            fruits.remove('cherry')
    
    print('The fruits that got removed are:')
    for fruit in fruits:
        print(