#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of words and returns user input. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    word = ''
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        if word in words:
            print(word)
        else:
            print('That word is not in the list')
    
