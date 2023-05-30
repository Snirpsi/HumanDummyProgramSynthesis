#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates numbers and multiplyes words. """    
    
    numbers = range(1,11)
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for number in numbers:
        for word in words:
            print(number*word)
    
