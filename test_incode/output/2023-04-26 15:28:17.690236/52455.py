#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers and removes words. """    
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    words = [
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'
    ]
    
    numbers_without_words = [
        number for number in numbers if number not in words
    ]
    
    print(numbers_without_words)
    
