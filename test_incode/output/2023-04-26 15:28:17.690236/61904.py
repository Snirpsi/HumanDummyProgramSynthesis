#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of numbers and adds a list of words. """    
    numbers = [1,2,3,4,5]
    words = ['one', 'two', 'three', 'four', 'five']
    
    numbers_words = zip(numbers, words)
    
    for number, word in numbers_words:
        print(number, word)
    
