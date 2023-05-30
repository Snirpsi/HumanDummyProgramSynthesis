#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    while True:
        words = [str(input('Enter a word: ')) for i in range(5)]
        print('Multiplication of words: ', end='')
        print(*words)
        print('