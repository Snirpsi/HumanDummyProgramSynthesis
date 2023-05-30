#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds user input or iterates over fruits. """    
    fruits = ['apple', 'banana', 'cherry', 'orange']
    
    # Add user input or iterate over fruits.
    fruits_iter = iter(fruits)
    
    # Print each fruit one at a time.
    for fruit in fruits_iter:
        print(fruit)
        
    # Print the final fruit.
    print(fruits_iter