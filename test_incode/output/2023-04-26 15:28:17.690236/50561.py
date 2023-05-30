#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits and enumerates a list of words. """    
    fruits = ['apple', 'banana', 'cherry']
    words = ['apple', 'banana', 'cherry']
    
    while True:
        fruit = input('Enter a fruit: ')
        word = input('Enter a word: ')
        
        if fruit in fruits and word in words:
            print('{} is a {}.'.format(fruit, word))
        else:
            print('{} is not a {}.'.format(fruit, word))
    
