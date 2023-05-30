#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and iterates over user input. """    
    
    # Get the list of numbers from the user
    numbers = input("Enter a list of numbers: ")
    
    # Convert the list of numbers to a list of integers
    numbers = [int(n) for n in numbers.split()]
    
    # Iterate over the list of integers
    for n in numbers:
        print(n)
        
    # Close the server
    