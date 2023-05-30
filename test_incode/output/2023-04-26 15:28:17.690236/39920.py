#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and converts user input. """    
    
    words = []
    
    while True:
        words.append(input('Enter a word: '))
        
        if words[-1] == 'quit':
            break
        
    print('The word was: {}'.format(', '.join(words)))
    
    
