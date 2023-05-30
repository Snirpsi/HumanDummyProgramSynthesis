#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words or multiplyes words. """    
    while True:
        word = input('Enter a word: ')
        multiplier = 1
        if word == 'quit':
            break
        elif word == 'multiply':
            multiplier = int(input('Enter a multiplier: ')) 
            print('The word multiplied by {} is: {}'.format(multiplier, word*multiplier))
        else:
            print('The word is: {}'.format(word))
