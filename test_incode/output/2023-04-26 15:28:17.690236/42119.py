#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        words.append(word)
        if word == 'q':
            break
    print('\n'.join(words))
