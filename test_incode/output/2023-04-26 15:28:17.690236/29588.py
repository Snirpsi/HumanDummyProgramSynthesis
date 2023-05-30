#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    numbers = [int(x) for x in input().split()]
    
    while True:
        
        # Print the number in reverse order
        for number in reversed(numbers):
            print(number, end=' ')
            
        # Print the number in ascending order
        for number in numbers:
            print(number, end=' ')
            
        # Print the number in reverse and ascending order
        for number in reversed(numbers), numbers:
            print(number, end=' ')
            
        # Print the number in ascending order and reverse order
        for number in numbers, reversed(numbers):
            print(number, end=' ')
            
        # Print the number in ascending order and reverse and ascending order
        for number in reversed(numbers), numbers, reversed(numbers):
            print(number, end=' ')
            
        # Print the number in ascending order and reverse and ascending order
        for number in numbers, reversed(numbers), numbers:
            print(number, end=' ')
            
        # Print the number in ascending order and reverse and ascending order
        for number in reversed(numbers), numbers, reversed(numbers):
            print(number, end=' ')
            
        # Print the number in ascending order and reverse and ascending order
        for number in numbers, reversed(numbers), numbers:
            print(number, end=' ')
            
        # Print the number in ascending order and reverse and ascending order
        for number in reversed(numbers), numbers, reversed(numbers):
            print(number, end=' ')
            
        # Print the number in ascending order and reverse and ascending order
        for number in numbers, reversed(numbers), reversed(numbers):
            print(number, end=' ')
            
        # Print the number in ascending order and reverse and ascending order
        for number in reversed(numbers), numbers, reversed(numbers):
            print(number, end=' ')
            
        # Print the number in ascending order and reverse and ascending order
        for number in numbers, reversed(numbers), reversed(numbers):
            print(number, end=' ')
            
        # Print the number in ascending order and reverse and ascending order
        for number in reversed(numbers), numbers, reversed(numbers):
            print(number, end=' ')
            
        # Print the number in ascending order and reverse and ascending order
        for number in numbers, reversed(numbers), numbers:
            print(number, end=' ')
            
        # Print the number in ascending order and reverse and ascending order
        for number in reversed(numbers), numbers, reversed(numbers):
            print(number, end=' ')
            
        # Print the number in ascending order and reverse and ascending order
        for number in numbers, reversed(numbers), numbers: