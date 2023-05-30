#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts user input and prints numbers. """    
    
    number = input("Enter a number: ")
    
    if number.isdigit():
        print(int(number))
    else:
        print("Not a number!")
        
