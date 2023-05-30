#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers and converts user input. """    
    
    number = int(input("Enter a number: "))
    
    number = add_numbers(number)
    
    number = convert_input(number)
    
    print(number)
    
