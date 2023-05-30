#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers and prints a list of words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        number = int(input('Enter a number: '))
        if number % 2 == 0:
            print('{} is an even number.'.format(word))
        else:
            print('{} is an odd number.'.format(word))
        print('')
    print('Thank you for using the 