#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of numbers or stores fruits. """    
    
    fruits = ['apple', 'banana', 'orange', 'mango']
    
    fruits_store = FruitStore(fruits)
    
    fruits_store.store()
    
    fruits_store.print_fruits()
    
    fruits_store.print_fruits_