#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers and prints numbers. """    
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    numbers = [int(n) for n in numbers]
    numbers = [n for n in numbers if n >= 0]
    print(numbers)

<|/ file filename=