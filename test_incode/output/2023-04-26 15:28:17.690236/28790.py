#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words and removes words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        words.append(word)
    
    words = remove_words(words)
    
    print('\n'.join(words))

<|/ file source=github ext=.py |>