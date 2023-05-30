#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words and iterates over numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for index, word in enumerate(words):
        print(word, 'is', numbers[index])
    
    print('Done!')
    
