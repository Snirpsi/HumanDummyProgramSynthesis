#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and converts a list of words. """    
    
    import sys
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            sys.exit()
        
        if word == '':
            continue
        
        words.append(word)
    
    print('\n'.join(words))

<|/ file source=github ext=.py |>