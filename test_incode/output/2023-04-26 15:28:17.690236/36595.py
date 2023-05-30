#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words and multiplyes fruits. """    
    while True:
        word = input('Enter a word: ')
        fruit = input('Enter a fruit: ')
        fruits = fruit.split(' ')
        fruits = [int(x) for x in fruits]
        fru