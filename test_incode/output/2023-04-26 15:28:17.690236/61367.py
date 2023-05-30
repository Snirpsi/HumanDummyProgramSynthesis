#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of words and multiplyes numbers. """    
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    numbers = [1, 2, 3, 4, 5]
    
    for word in words:
        for number in numbers:
            print(number * word)
            
