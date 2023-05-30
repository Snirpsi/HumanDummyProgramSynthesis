#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words or opens user input. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if len(words) == 2:
            break
    
    print('\n'.join(words))
    
