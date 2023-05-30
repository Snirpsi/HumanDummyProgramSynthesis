#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input and enumerates words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        words.append(word)
        
    print('\nWords:')
    
    for word in words:
        print(word)
        
    print('\nDone.')
    
