#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and stores user input. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'q':
            break
        
    print('\n'.join(words))
    
