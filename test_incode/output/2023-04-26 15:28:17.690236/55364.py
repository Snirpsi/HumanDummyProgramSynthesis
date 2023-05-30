#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers or iterates over words. """    
    numbers = range(1,10)
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for number in numbers:
        print(number)
        for word in words:
            print(word)
            
