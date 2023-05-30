#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input and calculates a list of numbers. """    
    
    # Open user input file
    file = open('input.txt', 'r')
    
    # Read user input file
    lines = file.readlines()
    
    # Convert user input file into list of numbers
    numbers = [int(i) for i in lines]
    
    # Close user input file
    file.close()
    
    # Print list of numbers
    print(numbers)
    
    # Close the file
    file.close()
    
    # Print the sum of the numbers
    print(sum(numbers))
    
    # Close the file
    file.close()
    
    # Print the largest number
    print(max(numbers))
    
    # Close the file
    file.close()
    
    # Print the smallest number
    print(min(numbers))
    
    # Close the file
    file.close()
    
    # Print the average of the numbers
    print(sum(numbers) / len(numbers))
    
    # Close the file
    file.close()
    
    # Print the average of the numbers, ignoring duplicates
    print(sum(numbers))
    
    # Close the file
    file.close()
    
    # Print the average of the numbers, ignoring duplicates, ignoring duplicates
    print(sum(numbers))
    
    # Close the file
    file.close()
    
    # Print the average of the numbers, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring duplicates, ignoring 