#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores fruits. """    
    fruits = ['apple', 'banana', 'orange', 'kiwi']
    
    fruits_store = FruitStore(fruits)
    
    fruits_store.store()
    
    fruits_store.retrieve()
    
    fruits_store.