#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            print('Bye!')
            break
        else:
            print(word)
    
