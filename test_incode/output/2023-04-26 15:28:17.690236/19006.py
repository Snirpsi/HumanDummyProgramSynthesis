#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input or multiplyes a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'done':
            break
        
        print('Multiplying ' + ', '.join(words))
        
        print('Enter a word: ')
        
        word