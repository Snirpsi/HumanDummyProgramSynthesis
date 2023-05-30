#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds user input or returns words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        words.append(word)
    
    return words

<|/ file source=github filename=