#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words. """    
    word = 'hello'
    multiplier = 1
    while word != 'exit':
        multiplier = multiplier * int(word)
        word = input('Enter a word: ')
        print('The word multiplied by %d is %s' % (multiplier, word))
