#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words or opens fruits. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            print('Goodbye!')
            break
        else:
            print(word)
            print('')
    
