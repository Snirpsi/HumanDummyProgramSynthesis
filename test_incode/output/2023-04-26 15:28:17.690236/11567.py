#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words and iterates over numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    for number in numbers:
        for word in words:
            print(word * number)
            
