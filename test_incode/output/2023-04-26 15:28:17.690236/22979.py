#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            words.append(word)
    print('Words: ', words)
    
