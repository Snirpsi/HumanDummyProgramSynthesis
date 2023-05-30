#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words and converts words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print(word.upper())
            
