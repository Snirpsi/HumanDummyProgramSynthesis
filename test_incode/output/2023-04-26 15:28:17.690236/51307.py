#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words and converts user input. """    
    
    while True:
        words = input('Enter a word: ')
        
        if words == 'exit':
            break
        
        words = words.split()
        
        print(' '.join(words))
        
    print('Goodbye!')
    
