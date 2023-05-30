#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print(convert_word(word))
