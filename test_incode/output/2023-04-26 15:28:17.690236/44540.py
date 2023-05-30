#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and iterates over user input. """    
    
    words = []
    
    while True:
        
        line = input('Enter a word: ')
        
        if line == 'q':
            break
        
        words.append(line)
        
    print('\n'.join(words))
    
