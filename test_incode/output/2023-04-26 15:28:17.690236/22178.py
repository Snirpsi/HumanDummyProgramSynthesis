#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5]
    
    for index, number in enumerate(numbers):
        print("The number {} is {}".format(index, number))
    
    print("\nThe last number in the list is", numbers[-1])
    
    print("\nThe first number in the list is", numbers[0])
    
    print("\nThe last number in the list is", numbers[-2])
    
    print("\nThe first number in the list is", numbers[