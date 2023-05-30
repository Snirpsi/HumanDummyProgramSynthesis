#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores fruits. """    
    fruits = ["apple", "banana", "cherry"]
    
    # Store fruits.
    fruits_store = FruitStore()
    fruits_store.store(fruits)
    
    # Print the fruits.
    fruits = fruits_store.get_fruits()
    print("The fruits are 