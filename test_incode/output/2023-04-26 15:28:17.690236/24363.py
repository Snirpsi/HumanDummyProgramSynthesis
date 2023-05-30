#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or enumerates a list of words. """    
    words = ['cat', 'dog', 'mouse']
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        if word in words:
            print(word)
        else:
            print('Invalid word.')
