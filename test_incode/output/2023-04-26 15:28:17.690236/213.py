#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds numbers. """    
    
    numbers = input("Enter numbers: ")
    
    numbers = list(map(int, numbers.split()))
    
    numbers = sum(numbers)
    
    print(numbers)
    
