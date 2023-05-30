#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    for fruit in fruits:
        if fruit == 'apple':
            fruits.remove('apple')
        elif fruit == 'banana':
            fruits.remove('banana')
        elif fruit == 'cherry':
            fruits.remove('cherry')
        else:
            print('Unknown fruit: ' + fruit)
            
    print('Done!')
    
