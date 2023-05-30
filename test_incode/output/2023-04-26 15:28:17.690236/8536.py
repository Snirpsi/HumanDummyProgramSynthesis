#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words. """    
    words = ['cat', 'dog', 'mouse', 'horse', 'lion', 'monkey', 'rabbit', 'sheep', 'tiger']
    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        
        if word in words:
            print('{} is a 