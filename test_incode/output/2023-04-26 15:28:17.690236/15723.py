#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers and converts numbers. """    
    
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    
    numbers_converted = []
    
    for number in numbers:
        number = int(number)
        numbers_converted.append(number)
    
    print(numbers_converted)
    
