#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input or converts a list of numbers. """    
    
    # Get the input from the user
    number = input("Enter a number: ")
    
    # Convert the input to a list of numbers
    numbers = [int(i) for i in number.split(",")]
    
    # Print the list
    print(numbers)
    
    # Iterate over the list
    for number in numbers:
        print(number)
        
    # 