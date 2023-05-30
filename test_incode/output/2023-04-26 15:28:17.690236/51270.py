#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    word = ''
    
    while True:
        word = input('Enter a word: ')
        
        if word == '':
            print('Goodbye!')
            break
        
        if word in words:
            print('Found it!')
            break
        
        print('Sorry, I don\'t know that word.')
        
    print('Goodbye!')
    
