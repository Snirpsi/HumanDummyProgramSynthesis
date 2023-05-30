#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words or returns words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print('You said: ' + word)
            print('I said: ' + word + '\n')
            print('')
    print('Bye')
