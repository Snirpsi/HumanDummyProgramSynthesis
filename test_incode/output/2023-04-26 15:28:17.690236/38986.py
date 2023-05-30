#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of numbers and enumerates words. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for index, number in enumerate(numbers):
        print("Number {}: {}".format(index, number))
    
    for word in words:
        print("Word {}: {}".format(word, number