#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words or stores user input. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        else:
            words.append(word)
    print('You entered', len(words), 'words')
    print('The word you entered was', words[len(words)-1], '