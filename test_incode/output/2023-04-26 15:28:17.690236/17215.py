#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers or calculates a list of words. """    
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    numbers_words = [numbers, words]
    
    for numbers_words in numbers_words:
        for number in numbers_words:
            for word in numbers_words:
                print(number * word)
