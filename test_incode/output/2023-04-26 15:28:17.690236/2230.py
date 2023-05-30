#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words and removes user input. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == '':
            break
        
        words.append(word)
    
    words = remove