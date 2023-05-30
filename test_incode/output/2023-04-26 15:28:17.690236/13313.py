#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns words and returns user input. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    
    return words
