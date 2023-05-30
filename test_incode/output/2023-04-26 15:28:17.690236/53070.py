#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates user input and adds words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        words.append(word)
    
    print('\n'.join(words))
    
