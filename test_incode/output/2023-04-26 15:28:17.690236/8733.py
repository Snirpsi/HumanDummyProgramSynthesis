#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words. """    
    words = ['hello', 'world', '!']
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        word = word.lower()
        if word in words:
            print(word + ' is 