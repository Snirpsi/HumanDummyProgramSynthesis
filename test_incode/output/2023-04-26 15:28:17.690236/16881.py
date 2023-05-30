#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of words and converts numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six']
    numbers = [1, 2, 3, 4, 5, 6]
    
    for word in words:
        for number in numbers:
            print(word, number)
        
