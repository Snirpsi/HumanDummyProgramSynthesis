#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words and prints user input. """    
    while True:
        words = input('Enter a word: ')
        if words:
            print(words)
        else:
            break
