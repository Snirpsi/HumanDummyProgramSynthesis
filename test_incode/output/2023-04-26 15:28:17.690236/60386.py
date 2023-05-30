#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words or prints a list of words. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        elif word == '':
            print('No word entered')
        else:
            print(words[words.index(word)], end=' ')
            
