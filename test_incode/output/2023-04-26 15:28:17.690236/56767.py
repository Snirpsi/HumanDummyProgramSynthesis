#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words. """    
    words = ['cat', 'dog', 'bird', 'horse', 'sheep', 'cow', 'pig']
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            print('Goodbye!')
            break
        if word in words:
            print('Found', word)
        else:
            print('Not found', word)
