#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        else:
            print(word.upper())
