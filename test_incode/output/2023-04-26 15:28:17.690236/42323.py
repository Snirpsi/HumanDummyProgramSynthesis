#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and converts user input. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        words.append(word)
    
    print('\n'.join(words))
    
