#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts user input or iterates over words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        words.append(word)
        
    print('\n'.join(words))
    
