#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input and returns a list of words. """    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        print('You entered', word)
        if word == 'quit':
            break
    print('You entered', word, 'and your words are', ', '.join(words))
    return words

<|/ file ext=.py |>