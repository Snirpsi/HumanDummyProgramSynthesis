#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores fruits. """    
    
    fruits = ['apple', 'banana', 'orange']
    
    fruits_store = FruitStore()
    
    for fruit in fruits:
        fruits_store.add_fruit(fruit)
    
    for fruit in fruits:
        print(