#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers or iterates over user input. """    
    
    # Read user input
    numbers = input("Enter a list of numbers: ")
    
    # Remove numbers from list
    numbers = numbers.split()
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    # Print result
    print(numbers)
    
    # Iterate over user input
    for number in numbers:
        print(number)
        
