#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input and returns a list of words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        words.append(word)
    print('The words 