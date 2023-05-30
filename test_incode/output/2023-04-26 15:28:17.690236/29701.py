#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input and calculates a list of words. """    
    
    words = []
    
    while True:
        line = input('Enter a word: ')
        
        if line == 'q':
            break
        
        words.append(line)
    
    print('\n'.join(words))
    
