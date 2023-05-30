#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words or adds user input. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        words.append(word)
    print('You entered', len(words), 'words')
    print('The 