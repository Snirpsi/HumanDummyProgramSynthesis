#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds user input or calculates a list of numbers. """    
    
    # Get the user input
    number = input("Enter a number: ")
    
    # Calculate the list of numbers
    numbers = []
    for number in number.split():
        numbers.append(int(number))
    
    # Print the list of numbers
    print(numbers)
    
    # Print the sum of the numbers
    print(sum(numbers))
    
    # Print the average of the numbers
    print(sum(numbers)/len(numbers))
    
    # Print the median of the numbers
    print(sorted(numbers)[len(numbers)//2])
    
    # Print the maximum of the numbers
    print(max(numbers))
    
    # Print the minimum of the numbers
    print(min(numbers))
    
    # Print the standard deviation of the numbers
    print(