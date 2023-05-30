#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input or removes words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        if word == '':
            continue
        print('The word "' + word + '" was found in this sentence.')
        print('The sentence 