#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        print('The word "{}" appears {} times.'.format(word, 
            len(set(word.split())))
        )
