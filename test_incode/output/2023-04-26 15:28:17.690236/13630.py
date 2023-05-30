#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words. """    
    words = ['apple', 'banana', 'cherry']
    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        else:
            print(word)
            
    print('\nThanks for playing!')
<|/ file ext=.py filename=