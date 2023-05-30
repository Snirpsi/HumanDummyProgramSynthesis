#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words and calculates words. """    
    while True:
        word = input("Enter a word: ")
        word_length = len(word)
        word_count = len(word.split())
        word_average = word_count / word_length
        word_average = word_average.