#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of words or returns user input. """    
    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for word in words:
        print(word)
    
    word = input('Enter a word: ')
    
    if word == 'quit':
        print('Goodbye!')
        
    else:
        print('You entered:', word)
    
