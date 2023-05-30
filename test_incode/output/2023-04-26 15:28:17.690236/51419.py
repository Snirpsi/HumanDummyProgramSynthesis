#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words or iterates over fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    for fruit in fruits:
        if fruit == 'cherry':
            fruits.remove(fruit)
        else:
            print('The fruit ' + fruit + ' is ' + fruit)
            
    print('Done')
    
