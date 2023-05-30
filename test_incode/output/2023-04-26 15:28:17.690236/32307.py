#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port and iterates over fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    for fruit in fruits:
        fruit = fruit.upper()
        
        if fruit == 'CHERRY':
            fruit = 'CHERRY PUFF'
            
        print('{} is {} and has {} apples.'.format(fruit, fruit, len(fruit