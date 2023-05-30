#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of numbers or adds numbers. """    
    
    # Create a list with 10 numbers in it
    numbers = [x for x in range(10)]
    
    # Add 10 numbers to the list
    numbers += range(10)
    
    # Print the list
    print(numbers)
    
    # Print the list again
    print(numbers)
    
    # Print the list with only odd numbers
    numbers = [x for x in range(10) if x % 2 == 0]
    print(numbers)
    
    # Print the list with only even numbers
    numbers = [x for x in range(10) if x % 2 == 1]
    print(numbers)
    
    # Print the list with only odd numbers and even numbers
    numbers = [x for x in range(10) if x % 2 == 0 and x % 2 == 1]
    print(numbers)
    
    # Print the list with only odd numbers and odd numbers
    numbers = [x for x in range(10) if x % 2 == 0 and x % 2 != 1]
    print(numbers)
    
    # Print the list with only odd numbers and odd numbers and odd numbers
    numbers = [x for x in range(10) if x % 2 == 0 and x % 2 != 1 and x % 2 != 2]
    print(numbers)
    
    # Print the list with only odd numbers and odd numbers and odd numbers and odd numbers
    numbers = [x for x in range(10) if x % 2 == 0 and x % 2 != 1 and x % 2 != 2 and x % 2 != 3]
    print(numbers)
    
    # Print the list with only odd numbers and odd numbers and odd numbers and odd numbers and odd numbers
    numbers = [x for x in range(10) if x % 2 == 0 and x % 2 != 1 and x % 2 != 2 and x % 2 != 3 and x % 2 != 4]
    print(numbers)
    
    # Print the list with only odd numbers and odd numbers and odd numbers and odd numbers and odd numbers and odd numbers
    numbers = [x for x in range(10) if x % 2 == 0 and x % 2 != 1 and x % 2 != 2 and x % 2 != 3 and x % 2 != 4 and x % 2 != 5]
    print(numbers)
    
    # Print the list with only odd numbers and odd numbers and odd numbers and odd numbers and odd numbers and odd numbers and odd numbers
    numbers = [x for x in range(10) if x % 2 == 0 and x % 2 != 1 and x % 2 != 2 and x % 2 != 3 and x % 2 != 4 and x % 2 != 5 and x % 2 != 6]
    print(numbers)
    
    # Print the list with only odd numbers and odd numbers and odd numbers and odd numbers and odd numbers and 