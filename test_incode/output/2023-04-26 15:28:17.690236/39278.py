#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers and returns a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        numbers = [number] * int(input("Enter number of numbers: "))
        print(numbers)
        
