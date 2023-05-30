#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers and adds a list of words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    numbers_words = []
    for number in numbers:
        numbers_words.append(str(number) + 