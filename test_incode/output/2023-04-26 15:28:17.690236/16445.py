#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    
    fruits_store = FruitStore(fruits)
    
    fruits_store.store()
    
    fruits_store.get_fruits()
    
    fruits_store.get_fruits(2)
    
    fruits_store.get_fruits(