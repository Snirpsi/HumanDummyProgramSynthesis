#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words or converts user input. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        words.append(word)
        
    print('\n'.join(' '.join(words).split()))
    
