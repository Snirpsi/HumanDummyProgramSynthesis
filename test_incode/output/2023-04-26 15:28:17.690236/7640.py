#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of numbers and converts a list of words. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    for index, number in enumerate(numbers):
        for word in words:
            print(number, word, end='