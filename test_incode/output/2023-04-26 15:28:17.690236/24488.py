#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or stores a list of words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        else:
            words.append(word)
    print('Words 