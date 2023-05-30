#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words or adds user input. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print(convert_words(word))

<|/ file source=github filename=