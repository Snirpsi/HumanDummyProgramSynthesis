#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input or stores a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    
    print('You entered', len(words), 'words')
    
    print('You entered', words[0], 'and', words[1], '