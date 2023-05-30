#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers. """    
    
    # Open the file with the numbers
    numbers = open('numbers.txt', 'r')
    
    # Read the numbers from the file
    numbers_str = numbers.read()
    
    # Split the numbers into an array
    numbers_array = numbers_str.split('\n')
    
    # Print the numbers
    for number in numbers_array:
        print(number)
    
    # Close the file
    numbers.close()
    
    # Close the program
    exit(0)
    
