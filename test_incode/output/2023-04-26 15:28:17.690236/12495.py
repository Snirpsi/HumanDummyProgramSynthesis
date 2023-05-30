#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words. """    
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            print('Goodbye!')
            break
        
        word = word.lower()
        
        if word == 'hello':
            print('Hello')
        elif word == 'world':
            print('World')
        else:
            print('That word is not recognized. Try again.')
    
