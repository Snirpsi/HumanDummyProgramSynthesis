#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input or prints words. """    
    while True:
        word = input('Enter a word: ')
        word = word.lower()
        word = word.split()
        word = ' '.join(word)
        print(word)
