#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers and adds a list of numbers. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    numbers_add = []
    
    # Loop over all numbers in the list
    for number in numbers:
        # Add the current number to the list of numbers to add
        numbers_add.append(number)
        
    # Print the list of numbers to stdout
    print(numbers_add)
    
    # 