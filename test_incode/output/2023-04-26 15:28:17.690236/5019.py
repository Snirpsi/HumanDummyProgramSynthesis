#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and iterates over a list of numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for word in words:
        for number in numbers:
            print(word + 