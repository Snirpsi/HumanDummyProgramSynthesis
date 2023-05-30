#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words or stores numbers. """    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        else:
            print(word)
            