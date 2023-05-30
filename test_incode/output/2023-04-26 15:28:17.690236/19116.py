#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and multiplyes a list of numbers. """    
    
    words = ['one', 'two', 'three', 'four', 'five']
    numbers = [1, 2, 3, 4, 5, 6]
    
    for word in words:
        for number in numbers:
            print(number * word)
        
