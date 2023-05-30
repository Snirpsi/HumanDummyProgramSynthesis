#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words and opens fruits. """    
    words = input('Enter a comma-separated list of words: ')
    fruits = open('fruits.txt', 'w')
    fruits.write(words)
    fruits.close()
    
