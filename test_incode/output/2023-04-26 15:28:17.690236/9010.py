#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words or converts a port. """    
    while True:
        word = input('Enter a word: ')
        word = word.lower()
        if word == 'exit':
            break
        else:
            print(word)
