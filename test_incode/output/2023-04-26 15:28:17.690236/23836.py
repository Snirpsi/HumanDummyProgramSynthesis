#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Calculate sum
    total = sum(numbers)
    
    # Calculate average
    average = total / len(numbers)
    
    # Print the average
    print("The average is", average)
    
    # Print the sum
    print("The sum is", total)
    
    # Print the list
    print("The list is", numbers)
    
    # Print the length of the list
    print("The length of the list is", len(numbers))
    
    # Print the length of the number
    print("The length of the number is", len(numbers[0]))
    
    # Print the length of the number in words
    print("The length of the number in words is", len(numbers[0]).split())
    
    # Print the length of the number in words in reverse
    print("The length of the number in words in reverse is", len(numbers[0]).rsplit())
    
    # Print the length of the number in words in reverse in reverse
    print("The length of the number in words in reverse in reverse is", len(numbers[0]).r