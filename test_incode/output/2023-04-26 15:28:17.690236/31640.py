#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    numbers = [int(i) for i in numbers]
    numbers.sort()
    print(numbers)
    
