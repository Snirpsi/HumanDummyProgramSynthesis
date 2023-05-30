#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    
    for number in numbers:
        if number.isdigit():
            numbers.remove(number)
    
    print(numbers)
    
