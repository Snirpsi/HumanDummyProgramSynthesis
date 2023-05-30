#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words or opens a list of numbers. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        elif word == '':
            print('No more words please.')
        else:
            print(word)
