#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input or returns words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            print(word)
