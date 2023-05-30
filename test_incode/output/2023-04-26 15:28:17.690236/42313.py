#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words or adds a list of words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        elif word == 'add':
            print('The word ' + word + ' has been added.')
        elif word == 'list':
            print('The word ' + word + ' has been listed.')
        else:
            print('The word ' + word + ' is not recognized.')
