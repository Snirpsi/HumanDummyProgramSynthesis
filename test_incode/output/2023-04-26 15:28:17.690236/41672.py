#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores user input and returns a list of words. """    
    
    word_list = []
    
    while True:
        
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        word_list.append(word)
        
    return word_list

<|/ file source=github filename=word_list.py |>