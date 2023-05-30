#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or returns a list of words. """    
    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        words.append(word)
    print('You entered', len(words), 'words')
    return words
    
