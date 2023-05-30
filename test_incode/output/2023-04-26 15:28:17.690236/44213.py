#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words. """    
    while True:
        word = str(input('Enter a word: '))
        word = word.lower()
        word = word.split()
        word = [word.index(i) for i in word]
        word = [i for i in word if i not in range(0,