#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            print('Goodbye!')
            break
        
        words.append(word)
    
    print('You entered:', words)
    
    