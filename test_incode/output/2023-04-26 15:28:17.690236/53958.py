#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input and iterates over words. """    
    while True:
        word = input('Enter a word: ')
        word = word.lower()
        word = word.split()
        
        for word in word:
            print(word)
            
