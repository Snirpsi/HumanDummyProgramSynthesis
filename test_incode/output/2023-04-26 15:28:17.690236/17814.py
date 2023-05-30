#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and opens words. """    
    
    words = []
    
    while True:
        line = input('Enter a word: ')
        
        if line == 'q':
            break
        
        words.append(line)
        
    print('\n'.join(words))
    
