#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        else:
            print(calc_words(word))
