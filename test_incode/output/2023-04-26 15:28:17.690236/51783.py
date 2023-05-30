#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input or iterates over a list of numbers. """    
    
    numbers = input("Enter numbers: ")
    
    # Iterate over the list of numbers
    for number in numbers:
        print(number)
        
    # Return the user input if there are no numbers
    if len(numbers) == 0:
        print("No numbers entered")
        
    # Return the user input if there are multiple numbers
    elif len(numbers) > 1:
        print("Multiple numbers entered")
        
    else:
        print("Invalid input")
        
    
