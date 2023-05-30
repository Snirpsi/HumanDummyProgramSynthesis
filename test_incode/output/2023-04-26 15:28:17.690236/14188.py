#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or converts user input. """    
    
    # Get the input from the user
    number = int(input("Enter a number: "))
    
    # Convert the input to a list of numbers
    numbers = list(map(int, input("Enter a number: ")))
    
    # Print the list
    print("The list is:")
    print(numbers)
    
    # Print the converted number
    print("The converted number is:")
    print(number