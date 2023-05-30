#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers. """    
    numbers = [int(i) for i in input().split()]
    
    # Store the numbers in reverse order
    numbers.reverse()
    
    # Print the numbers
    for number in numbers:
        print(number)
        
    # Print the numbers reversed
    for number in reversed(numbers):
        print(number)
    
    # Print the numbers reversed in reverse
    for number in reversed(reversed(numbers)):
        print(number)
    
    # Print the numbers reversed in reverse order
    for number in reversed(reversed(numbers)):
        print(number)
    
    # Print the numbers reversed in reverse order and store in reverse
    for number in reversed(reversed(reversed(numbers))):
        print(number)
    
    # Print the numbers reversed in reverse order and store in reverse order
    for number in reversed(reversed(reversed(reversed(numbers))