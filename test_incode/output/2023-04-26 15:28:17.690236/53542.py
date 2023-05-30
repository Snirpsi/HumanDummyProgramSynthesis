#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over fruits and adds a list of words. """    
    fruits = ['apple', 'banana', 'cherry']
    words = ['word1', 'word2']
    for fruit in fruits:
        for word in words:
            print(word + ' ' + fruit)
