#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits. """    
    
    fruits = ['apple', 'banana', 'cherry', 'orange', 'pear', 'pineapple', 'plum']
    
    for fruit in fruits:
        
        if fruit == 'apple':
            fruits.remove('apple')
            
        if fruit == 'banana':
            fruits.remove('banana')
            
        if fruit == 'cherry':
            fruits.remove('cherry')
            
        if fruit == 'orange':
            fruits.remove('orange')
            
        if fruit == 'pear':
            fruits.remove('pear')
            
        if fruit == 'pineapple':
            fruits.remove('pineapple')
            
        if fruit == 'plum':
            fruits.remove('plum')
            
    print('The fruits have been removed')
    
