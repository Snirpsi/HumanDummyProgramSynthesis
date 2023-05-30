#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words or converts user input. """    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            print('Goodbye!')
            break
        else:
            print('You entered', word)
