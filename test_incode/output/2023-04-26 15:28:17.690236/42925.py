#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    print('\n'.join(words))
    
