#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words or adds numbers. """    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        if word == 'qwertyuiop':
            print('Bye')
            break
        print('