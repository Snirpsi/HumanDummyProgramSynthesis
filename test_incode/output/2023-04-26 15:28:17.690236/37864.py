#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input or multiplyes a list of words. """    
    while True:
        word = input('Enter a word: ')
        multiplied = []
        for word in word.split(' '):
            multiplied.append(int(word) * 2)
        print(multiplied)
