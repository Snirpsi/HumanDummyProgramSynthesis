#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words or multiplyes numbers. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        elif word == 'quit\n':
            print('Bye!')
            break
        else:
            print(word*2)
