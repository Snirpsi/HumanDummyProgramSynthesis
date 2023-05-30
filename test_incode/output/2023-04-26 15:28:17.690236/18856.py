#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input or multiplyes numbers. """    
    
    number = input("Enter a number: ")
    
    if number.isdigit():
        number = int(number)
        print(number * 2)
    else:
        print("Invalid input")
        
