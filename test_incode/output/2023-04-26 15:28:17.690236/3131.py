#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words or opens user input. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'done':
            break
        
        words.append(word)
        
    print('\n'.join(words))
    
