#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input or removes a list of words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        else:
            words.append(word)
    print('The words 