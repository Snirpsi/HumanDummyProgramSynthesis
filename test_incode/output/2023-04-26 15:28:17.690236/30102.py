#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits. """    
    
    fruits = ['apple', 'banana', 'orange', 'mango', 'pineapple', 'peach', 'plum']
    
    for fruit in fruits:
        
        fruits.remove(fruit)
        
    print('The fruits are:')
    
    for fruit in fruits:
        print(fruit)
        
    print('Done.')
    
