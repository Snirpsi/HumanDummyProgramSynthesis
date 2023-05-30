#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over numbers and prints user input. """    
    
    numbers = [int(i) for i in input("Enter numbers: ").split()]
    
    for number in numbers:
        print(number)
        
