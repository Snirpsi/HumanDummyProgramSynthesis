#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input and stores words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        words.append(word)
    print('Words: ', ', '.join(words))
    
