#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers and calculates words. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Iterate over the numbers and calculate the words for each number
    for number in numbers:
        print("The word for number {} is {}".format(number, 