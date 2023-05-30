#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or iterates over user input. """    
    
    words = []
    
    while True:
        
        line = input('Enter a word: ')
        
        if line == 'q':
            break
        
        words.append(line)
        
    print('\n'.join(words))
    
