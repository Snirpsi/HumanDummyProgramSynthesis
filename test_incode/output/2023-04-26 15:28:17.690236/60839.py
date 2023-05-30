#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of numbers and enumerates user input. """    
    
    # Get the list of numbers and enumerate them
    numbers = list(range(1,101))
    enumerated_numbers = list(enumerate(numbers))
    
    # Print the results
    print("Numbers:")
    for index, number in enumerated_numbers:
        print("{}. {}".format(index, number))
    
    # Print the enumerated numbers
    print("Enumerated numbers:")
    for index, number in enumerated_numbers:
        print("{}. {}".format(index, number))
    
    # Print the enumerated numbers and their index
    print("Enumerated numbers and their index:")
    for index, number in enumerated_numbers:
        print("{}. {}. {}".format(index, number, index))
    
    # Print the enumerated numbers and their index and their value
    print("Enumerated numbers and their index and their value:")
    for index, number in enumerated_numbers:
        print("{}. {}. {}. {}".format(index, number, index, number))
    
    # Print the enumerated numbers and their index and their value and their value
    print("Enumerated numbers and their index and their value and their value:")
    for index, number in enumerated_numbers:
        print("{}. {}. {}. {}. {}. {}".format(index, number, index, number, index, number))
    
    # Print the enumerated numbers and their index and their value and their value and their value
    print("Enumerated numbers and their index and their value and their value and their value:")
    for index, number in enumerated_numbers:
        print("{}. {}. {}. {}. {}. {}. {}. {}".format(index, number, index, number, index, number, index, number, index, number))
    
    # Print the enumerated numbers and their index and their value and their value and their value and their value
    print("Enumerated numbers and their index and their value and their value and their value and their value:")
    for index, number in enumerated_numbers:
        print("{}. {}. {}. {}. {}. {}. {}. {}. {}. {}. {}".format(index, number, index, number, index, number, index, number, index, number, index, number, index, number))
    
    # Print the enumerated numbers and their index and their value and their value and their value and their value
    print("Enumerated numbers and their index and their value and their value and their value and their value and their value:")
    for index, number in enumerated_numbers:
        print("{}. {}. {}. {}. {}. {}. {}. {}. {}. {}. {}. {}. {}".format(index, number, index, number, index, number, index, number, index, number, index, number, index, number, index, number, index, number))
    
    # Print the enumerated numbers and their index and their value and their value and their 