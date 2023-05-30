#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates user input and returns a list of words. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        if word == 'q':
            break
        words.append(word)
    
    return words

<|/ file source=github ext=.py filename=word_count.py |>