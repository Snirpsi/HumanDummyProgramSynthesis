#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers and multiplyes a list of words. """    
    while True:
        numbers = [int(x) for x in input('Enter a number: ').split()]
        words = [int(x) for x in input('Enter a word: ').split()]
        numbers = numbers * words
        print('The product of %d and %d is %d.'
              % (numbers[0], numbers[1], numbers[2]))
        
