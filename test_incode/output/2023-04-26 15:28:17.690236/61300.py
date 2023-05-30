#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and adds a list of numbers. """    
    words = ['word1', 'word2', 'word3']
    numbers = [1, 2, 3]
    
    for word in words:
        for number in numbers:
            print(word, number)
        
