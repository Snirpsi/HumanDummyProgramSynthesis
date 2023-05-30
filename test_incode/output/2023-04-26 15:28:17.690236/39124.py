#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words. """    
    import sys
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        if word not in words:
            words.append(word)
    
    print('\n'.join(words))
    
