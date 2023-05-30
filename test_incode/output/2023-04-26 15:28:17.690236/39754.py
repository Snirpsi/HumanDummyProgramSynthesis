#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'snake', 'bird']
    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        else:
            print(words[words.index(word)], end=' ')
