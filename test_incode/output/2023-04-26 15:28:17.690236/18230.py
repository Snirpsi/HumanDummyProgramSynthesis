#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words and returns user input. """    
    words = []
    while True:
        words.append(input('Enter a word: '))
        if words[-1] == 'q':
            break
    return words
