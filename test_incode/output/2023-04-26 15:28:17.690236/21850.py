#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of numbers or stores numbers. """    
    
    # Iterate over all numbers in the list
    for num in nums:
        print(num)
        
    # Store all numbers in a list
    numbers = [num for num in nums]
    
    # Print the list
    print(numbers)
    
    # Print the list as a string
    print(str(numbers))
    
    # Print the list as a list of strings
    print(str(numbers).split())
    
    # Print the list as a list of integers
    print(str(numbers).split(','))
    
    # Print the list as a list of floats
    print(str(numbers).split('.'))
    
    # Print the list as a list of tuples
    print(str(numbers).split('('))
    
    # Print the list as a list of dictionaries
    print(str(numbers).split('