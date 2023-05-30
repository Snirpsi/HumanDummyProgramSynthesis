#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Remove all numbers between 3 and 10
    while len(numbers) > 3:
        numbers.remove(numbers[3])
    
    # Print the remaining numbers
    print(numbers)
    
    # 