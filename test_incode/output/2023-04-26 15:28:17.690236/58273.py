#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers. """    
    
    # Create a list with 10 elements:
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    # Print the list:
    print(numbers)
    
    # Add two numbers:
    numbers[0] = numbers[0] + numbers[1]
    
    # Print the list:
    print(numbers)
    
    # Print the sum of the list:
    print(sum(numbers))
    
    # Print the average of the list:
    print(sum(numbers) / len(numbers))
    
    # Print the maximum of the list:
    print(max(numbers))
    
    # Print the minimum of the list:
    print(min(numbers))
    
    # Print the standard deviation of the list:
    print(