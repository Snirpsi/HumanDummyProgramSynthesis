#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and prints a list of words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q': break
        words.append(word)
    print('\n'.join(words))
