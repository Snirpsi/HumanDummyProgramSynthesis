#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input and stores a list of words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        words.append(word)
    print('The words are: ', ', '.join(words))
    
