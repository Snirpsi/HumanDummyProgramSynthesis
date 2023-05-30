#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words. """    
    words = ['cat', 'dog', 'bird', 'snake', 'mouse', 'elephant']
    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        
        word = word.lower()
        
        if word in words:
            print(word + ' is a 