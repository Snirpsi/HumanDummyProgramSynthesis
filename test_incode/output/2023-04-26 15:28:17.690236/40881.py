#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input or stores a list of words. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    
    print('\n'.join(words))
    
