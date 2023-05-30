#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over numbers and returns a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Iterate over numbers and add them to a list.
    numbers_plus_one = []
    for number in numbers:
        numbers_plus_one.append(number + 1)
    
    # Print the list.
    print(numbers_plus_one)
    
    # Iterate over numbers and print each number with a different name.
    for number in numbers:
        print(number + 