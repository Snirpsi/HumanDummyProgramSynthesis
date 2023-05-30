#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words. """    
    while True:
        word = str(input('Enter a word: '))
        word = list(word)
        word.append(word)
        word = ''.join(word)
        print('The word is', word)
