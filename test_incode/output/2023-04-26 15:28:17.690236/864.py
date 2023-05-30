#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words. """    
    while True:
        word = input('Enter a word: ')
        print('The word is', word)
        if word == 'quit':
            print('Goodbye!')
            break
        else:
            print('