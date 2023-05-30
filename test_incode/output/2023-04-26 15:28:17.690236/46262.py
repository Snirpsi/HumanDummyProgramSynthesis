#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns numbers and prints fruits. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    
    # Create a list to store our fruits.
    fruitList = []
    
    # Iterate through our fruits and add them to the list.
    for fruit in fruits:
        fruitList.append(fruit)
    
    # Print out our fruits.
    for fruit in fruitList:
        print(fruit)
        
    # Print out how many times each fruit appears.
    for fruit in fruitList:
        print(fruit, 