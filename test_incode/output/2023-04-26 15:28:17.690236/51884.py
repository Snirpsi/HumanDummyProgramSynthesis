#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits. """    
    fruits = open_fruits()
    
    # A function that prints out the contents of the fruits list
    def print_fruits(fruits):
        for fruit in fruits:
            print(fruit)
    
    # A function that prints out the contents of the fruits list
    def print_fruits_reversed(fruits):
        for fruit in fruits[::-1]:
            print(fruit)
    
    # A function that prints out the contents of the fruits list
    def print_fruits_reversed_reversed(fruits):
        for fruit in fruits[::-1]:
            for fru