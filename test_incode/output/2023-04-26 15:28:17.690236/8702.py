#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores fruits. """    
    fruits = ['apple', 'orange', 'banana']
    
    fruits_store = FruitStore()
    fruits_store.add(fruits)
    
    for fruit in fruits:
        print(fruit)
    
    fruits_store.