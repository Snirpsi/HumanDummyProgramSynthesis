#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input or iterates over a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        words.append(word)
        
    print('\n'.join(' '.join(word) for word in words))
    
