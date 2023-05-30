#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers. """    
    
    # Create a list with 10 numbers from 1 to 10
    numbers = [x for x in range(1, 11)]
    
    # Print the list
    print(numbers)
    
    # Print the sum of the numbers
    print(sum(numbers))
    
    # Print the average of the numbers
    print(sum(numbers) / len(numbers))
    
    # Print the maximum of the numbers
    print(max(numbers))
    
    # Print the minimum of the numbers
    print(min(numbers))
    
    # Print the standard deviation of the numbers
    print(