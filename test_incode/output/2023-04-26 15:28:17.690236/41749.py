#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns numbers or multiplyes numbers. """    
    
    numbers = input("Enter numbers: ")
    
    if numbers.isdigit():
        numbers = int(numbers)
    else:
        print("Invalid input")
        
    numbers_multiplied = 1
    
    for number in numbers:
        numbers_multiplied *= number
    
    print(numbers_multiplied)
    
