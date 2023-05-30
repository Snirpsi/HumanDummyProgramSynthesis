#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words and iterates over words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            words = word.split()
            for word in words:
                print(word)
                