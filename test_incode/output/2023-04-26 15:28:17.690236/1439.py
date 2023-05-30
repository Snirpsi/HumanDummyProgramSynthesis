#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes user input or iterates over fruits. """    
    
    fruits = input("Enter fruits: ")
    
    if fruits == "quit":
        print("Goodbye!")
        exit()
    
    for fruit in fruits.split(","):
        print("Fruit is", fruit)
        
    
