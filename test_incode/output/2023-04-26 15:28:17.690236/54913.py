#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words. """    
    while True:
        words = input('Enter a word: ')
        words = words.split()
        words = [x*y for x,y in zip(words, words)]
        print(' '.join(words))
        
