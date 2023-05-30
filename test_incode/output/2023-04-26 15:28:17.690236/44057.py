#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'pear']
    
    fruits_store = FruitStore()
    
    for fruit in fruits:
        fruits_store.add(fruit)
    
    for fruit in fruits:
        print(