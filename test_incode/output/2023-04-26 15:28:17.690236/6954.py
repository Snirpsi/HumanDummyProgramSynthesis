#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    
    while True:
        numbers = input("Enter numbers: ")
        if numbers.isdigit():
            numbers = [int(n) for n in numbers.split()]
            print(numbers)
        else:
            break
    
