#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words or converts fruits. """    
    fruits = ["apple", "orange", "mango", "banana", "cherry"]
    
    # Convert fruits to integers
    fruits_int = [int(fruit) for fruit in fruits]
    
    # Multiply each integer by its corresponding fruit 