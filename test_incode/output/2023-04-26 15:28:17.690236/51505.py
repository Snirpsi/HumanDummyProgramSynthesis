#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input and adds a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        words.append(word)
        
    print('\n'.join(words))
    
