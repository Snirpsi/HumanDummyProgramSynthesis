#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    for fruit in fruits:
        
        if fruit == 'apple':
            fruits.remove('apple')
        
        else:
            fruits.remove(fruit)
            
    print('The fruits are now', fruits)
    
