#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words or converts numbers. """    
    while True:
        word = input('Enter a word: ')
        number = input('Enter a number: ')
        number = int(number)
        word = word.upper()
        number = int(number)
        word = word.lower()
        if word == 'exit':
            break
        elif word == 'multiply':
            number = number * number
            print('The product of {} and {} is {}.'.format(number, number, number))
        elif word == 'convert':
            number = int(number)
            print('The number {} is {}.'.format(number, number))
        else:
            print('Invalid input.')
