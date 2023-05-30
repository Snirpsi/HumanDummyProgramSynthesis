#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words or stores user input. """    
    
    words = ['hello', 'world', '!']
    
    while(True):
        word = input('Enter a word: ')
        
        if word in words:
            print(word + ' is a word!')
        else:
            print(word + ' is not a word!')
    
