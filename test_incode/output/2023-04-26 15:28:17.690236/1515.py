#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers and multiplyes a list of words. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    for number in numbers:
        for word in words:
            print(number * word, end='