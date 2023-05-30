#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and prints a port. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if len(words) == 3:
            break
    
    print('\n'.join(words))
    
    print('\nThe word 