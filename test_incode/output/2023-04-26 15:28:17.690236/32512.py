#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of numbers and converts user input. """    
    numbers = [int(n) for n in input("Enter a list of numbers: ").split()]
    
    # Print the list of numbers and the converted numbers
    print("The list of numbers are:")
    for n in numbers:
        print(n)
    print("The converted numbers are:")
    for n in numbers:
        print(int(n))
    
    # Print the list of numbers and the converted numbers, in reverse order
    print("The list of numbers are:")
    for n in reversed(numbers):
        print(n)
    print("The converted numbers are:")
    for n in reversed(numbers):
        print(int(n))
    
    # Print the list of numbers and the converted numbers, in reverse order, using reversed
    print("The list of numbers are:")
    for n in reversed(reversed(numbers)):
        print(n)
    print("The converted numbers are:")
    for n in reversed(reversed(numbers)):
        print(int(n))
    
    # Print the list of numbers and the converted numbers, in reverse order, using reversed
    print("The list of numbers are:")
    for n in reversed(reversed(reversed(numbers))):
        print(n)
    print("The converted numbers are:")
    for n in reversed(reversed(reversed(numbers))):
        print(int(n))
    
    # Print the list of numbers and the converted numbers, in reverse order, using reversed
    print("The list of numbers are:")
    for n in reversed(reversed(reversed(reversed(numbers))