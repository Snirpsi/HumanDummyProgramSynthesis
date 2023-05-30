#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers and returns fruits. """    
    import sys
    import random
    
    fruits = []
    
    # Generate a random list of numbers and add it to the fruits list.
    for num in range(1, 101):
        fruits.append(num)
        
    # Print the list of fruits.
    for fruit in fruits:
        print(fruit)
        
    # Print the list of numbers and return them to the user.
    print("\nThe list of numbers is as follows: ")
    for num in fruits:
        print(num)
        
    sys.exit(0)
    
