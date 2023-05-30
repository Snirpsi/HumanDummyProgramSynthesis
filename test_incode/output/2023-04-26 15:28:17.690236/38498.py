#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words or calculates fruits. """    
    while True:
        word = input('Enter a word: ')
        fruit = input('Enter a fruit: ')
        if word == 'exit':
            print('Goodbye!')
            break
        else:
            print('{} is a {}'.format(word, fruit))
