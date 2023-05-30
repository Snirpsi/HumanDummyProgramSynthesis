#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words and prints fruits. """    
    words = open('words.txt').read().split()
    fruits = ['apple', 'orange', 'pear', 'banana', 'cherry']
    for word in words:
        if word in fruits:
            print(word)
        else:
            print('No fruit 