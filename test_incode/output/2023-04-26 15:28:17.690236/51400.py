#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and multiplyes words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        else:
            words.append(word)
    multiplied = 0
    for word in words:
        multiplied += word
    print('The word multiplied by {} is {}'.format(multiplied, word