#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers or multiplyes numbers. """    
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    numbers = map(int, numbers)
    numbers = map(lambda x: x * 2, numbers)
    print(numbers)
    
