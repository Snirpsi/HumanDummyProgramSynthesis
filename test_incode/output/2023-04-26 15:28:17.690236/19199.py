#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words or prints a list of numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    word = ''
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        if word in words:
            print(words.index(word))
        else:
            print('Not a valid word.')
    
    print('Done.')
    
