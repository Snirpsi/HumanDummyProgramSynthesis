#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits and enumerates words. """    
    
    fruit = input("Enter a fruit: ")
    
    fruit = fruit.lower()
    
    fruits = fruit.split()
    
    for fruit in fruits:
        if fruit not in fruits:
            print(fruit, end=" ")
        else:
            print(fruit, end=" ")
            
