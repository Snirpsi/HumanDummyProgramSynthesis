#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words. """    
    while True:
        word = input('Enter a word: ')
        word = word.lower()
        word = word.split()
        word = [word.index(i) for i in word]
        word = [word[i] * word[i+1] for i in range(len(word) - 1)]
        print(' '.join(word))
