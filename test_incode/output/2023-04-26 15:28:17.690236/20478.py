#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    # Store the numbers in a list
    numbers_store = numbers[:]
    
    # Print the stored numbers
    print(numbers_store)
    
    # Remove the stored numbers from the list
    numbers_store = numbers_store[: