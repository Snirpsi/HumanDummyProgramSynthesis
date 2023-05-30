#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of numbers and iterates over a list of words. """    
    words = ['apple', 'banana', 'cherry']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for index, word in enumerate(words):
        print(index, word)
        for index, number in enumerate(numbers):
            print(index, number)
            
