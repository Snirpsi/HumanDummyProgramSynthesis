#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    for fruit in fruits:
        fruit = fruit.lower()
        
        if fruit == 'apple':
            print('apple')
        elif fruit == 'orange':
            print('orange')
        elif fruit == 'banana':
            print('banana')
        elif fruit == 'cherry':
            print('cherry')
        else:
            print('unknown fruit')
            
    print('done')
    
