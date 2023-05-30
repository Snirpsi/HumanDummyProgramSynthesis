#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and opens words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        else:
            words.append(word)
    print('\n'.join(words))
    
