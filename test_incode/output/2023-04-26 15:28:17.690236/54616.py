#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        words.append(word)
        print('The word is', word)
    print('The words were', words)
    
