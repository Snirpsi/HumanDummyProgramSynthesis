#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words or enumerates user input. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            words.append(word)
    print('\n'.join(words))
    
