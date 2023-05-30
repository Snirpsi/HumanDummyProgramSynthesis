#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or prints a list of words. """    
    
    words = []
    
    while True:
        line = input('Enter a word: ')
        words.append(line)
        
        if line == 'q':
            break
        
    print('\n'.join(words))
    
