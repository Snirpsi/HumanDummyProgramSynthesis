#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or prints a list of numbers. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        number = input("Enter a number: ")
        
        if number == 'done':
            break
        
        if number in fruits:
            print(number)
        else:
            print("Invalid number. Try again.")
    
