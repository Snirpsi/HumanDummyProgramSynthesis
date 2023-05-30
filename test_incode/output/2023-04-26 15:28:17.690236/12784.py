#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input and enumerates words. """    
    
    words = []
    
    while True:
        line = input('Enter a word: ')
        
        if line == 'quit':
            break
        
        if line == '':
            continue
        
        words.append(line)
        
    print('\n'.join(words))
    
