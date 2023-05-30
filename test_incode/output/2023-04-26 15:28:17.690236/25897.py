#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of words or prints a list of numbers. """    
    
    # iterate over all words in the list
    for word in words:
        print(word)
    
    # iterate over all numbers in the list
    for number in numbers:
        print(number)
    
    # iterate over all words and numbers in the list
    for word, number in zip(words, numbers):
        print(word, number)
    
    # iterate over all words and numbers in the list with a generator
    for word, number in words_and_numbers(words):
        print(word, number)
    
    # iterate over all words and numbers in the list with a generator 
    for word, number in words_and_numbers(numbers):
        print(word, number)
    
    # iterate over all words and numbers in the list with a generator 
    for word, number in words_and_numbers(numbers, 