#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input and prints numbers. """    
    
    numbers = input("Enter numbers: ")
    
    numbers = numbers.split()
    
    for number in numbers:
        print(number)
        
