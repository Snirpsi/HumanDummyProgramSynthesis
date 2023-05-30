#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input and adds fruits. """    
    
    # Get the fruits from the user
    fruits = input("Enter the fruits: ").split()
    
    # Iterate over the fruits adding them to the fruits_list list
    for fruit in fruits:
        fruits_list.append(fruit)
        
    # Print the fruits_list list
    print(fruits_list)
    
    # Print the fruits_list length
    print(fruits_