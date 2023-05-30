#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        words.append(word)
    print('You entered', len(words), 'words')
    print('You entered', words[0], 'and', words[-1], '