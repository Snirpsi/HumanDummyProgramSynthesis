#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    fruits_store = FruitStore()
    
    for fruit in fruits:
        fruits_store.add(fruit)
    
    for fruit in fruits:
        print('