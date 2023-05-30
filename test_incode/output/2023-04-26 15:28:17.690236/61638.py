#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers and iterates over user input. """    
    
    # Create a list with numbers from 1 to 10
    numbers = list(range(1, 11))
    
    # Print the numbers in the list
    print('The numbers in the list are:')
    for number in numbers:
        print(number)
    
    # Print the length of the list
    print('The length of the list is', len(numbers))
    
    # Print the length of the list with negative numbers
    print('The length of the list with negative numbers is ', len(numbers) 