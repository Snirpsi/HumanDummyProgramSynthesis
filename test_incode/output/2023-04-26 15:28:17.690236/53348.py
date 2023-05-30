#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words. """    
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        else:
            word = word.lower()
            word = word.split()
            for word in word:
                print(word)
