#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores user input and stores words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        words.append(word)
    
    print('\n'.join(words))
    
