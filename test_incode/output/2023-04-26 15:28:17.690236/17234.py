#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of numbers and iterates over user input. """    
    
    numbers = input("Enter a list of numbers: ")
    
    numbers = list(map(int, numbers.split()))
    
    numbers_sum = 0
    
    for number in numbers:
        numbers_sum += number
        
    print(numbers_sum)
    
