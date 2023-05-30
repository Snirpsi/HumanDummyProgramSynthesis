#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words. """    
    words = ['cat', 'dog', 'mouse']
    while True:
        word = input('Enter a word: ')
        if word not in words:
            print('Sorry, that word is not in the list')
        else:
            print(word)
