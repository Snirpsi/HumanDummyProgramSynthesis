#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input or converts words. """    
    while True:
        word = input('Enter a word: ')
        word = word.lower()
        word = word.capitalize()
        word = word.split()
        word = ' '.join(word)
        print(word)
