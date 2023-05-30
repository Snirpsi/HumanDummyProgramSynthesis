#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words and iterates over a list of numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for number in numbers:
        for word in words:
            print(word*number)
    
    print('\nDone.')
    
