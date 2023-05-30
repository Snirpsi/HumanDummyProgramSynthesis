#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input or adds a list of words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            print('Goodbye!')
            break
        else:
            print('You typed: ', word)
            print('