#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers and opens a list of numbers. """    
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    numbers = [int(n) for n in numbers]
    numbers.sort()
    numbers.reverse()
    print(numbers)
    
