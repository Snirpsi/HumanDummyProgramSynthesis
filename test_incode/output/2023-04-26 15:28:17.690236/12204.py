#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words and opens user input. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        words.append(word)
    
    print('\n'.join(words))
    
