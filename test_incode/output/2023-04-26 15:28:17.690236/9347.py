#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of numbers or returns user input. """    
    
    numbers = input("Enter numbers: ").split()
    
    if len(numbers) == 0:
        print("No numbers entered")
    else:
        print(