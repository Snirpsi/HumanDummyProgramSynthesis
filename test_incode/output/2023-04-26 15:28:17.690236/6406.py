#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words or adds words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print('You typed: ', word)
            print('You said: ', 