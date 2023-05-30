#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while True:
        word = input('Enter a word: ')
        if word not in words:
            print('That word is not in the list')
        else:
            print('That word is in the list')
