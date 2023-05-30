#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words or prints fruits. """    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        else:
            print('The word is', word, 'multiplied by ', end='')
            print(word, '=', end='')
            print(word*