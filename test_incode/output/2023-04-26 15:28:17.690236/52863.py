#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'exit':
            print('Goodbye!')
            break
        
        if word in words:
            print('Found it!')
        else:
            print('Sorry, I don\'t know that word.')
            
        print('')
        
