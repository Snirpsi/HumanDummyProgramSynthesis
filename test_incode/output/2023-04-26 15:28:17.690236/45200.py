#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words and iterates over fruits. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            print('Goodbye!')
            break
        else:
            fruit = input('Enter a fruit: ')
            if fruit == 'quit':
                print('Goodbye!')
                break
            else:
                print('You entered ' + fruit + ' and the word ' + word + ' is ' + 