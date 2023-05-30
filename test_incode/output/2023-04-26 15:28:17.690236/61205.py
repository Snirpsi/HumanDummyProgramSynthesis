#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words and multiplyes user input. """    
    words = []
    multiplier = 1
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        words.append(word)
        multiplier = multiplier * int(word)
    print(' '.join(words))
    print('The product of all the words is 