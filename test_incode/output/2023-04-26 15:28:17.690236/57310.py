#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers or converts fruits. """    
    
    # Convert numbers to fruits
    fruits = convert_numbers_to_fruits(1)
    
    # Convert fruits to numbers
    numbers = convert_fruits_to_numbers(fruits)
    
    # Print the numbers
    print(numbers)
    
    # Print the fruits
    print(fruits)
    
    # Print the fruits converted to numbers
    print(convert_fruits_to_numbers(fruits))
    
    # Print the fruits converted to numbers converted to numbers
    print(convert_fruits_to_numbers(convert_fruits_to_numbers(fruits))