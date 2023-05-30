#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds fruits and stores user input. """    
    
    fruits = input("Enter the fruits you want to add: ")
    
    fruits = fruits.split()
    
    for fruit in fruits:
        fruit = fruit.lower()
        
        if fruit not in fruits:
            print("Invalid fruit")
    
    fruits_set = set(fruits)
    
    for fruit in fruits_set:
        fruit = fruit.lower()
        
        if fruit not in fruits:
            print("Invalid fruit")
    
    fruits_set.discard(fruit)
    
    fruits_set.