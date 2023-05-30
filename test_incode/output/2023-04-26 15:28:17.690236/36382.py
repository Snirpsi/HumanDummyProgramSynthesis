#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        print('*' * 20)
        print(word)
        print('*' * 20)
        print('')
    print('Done')
