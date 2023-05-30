#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words. """    
    words = ['hello', 'world', '!']
    
    while True:
        word = input('> ')
        if word == 'q':
            break
        
        if word in words:
            print('{} is a word'.format(word))
        else:
            print('{} is not a word'.format(word))
            
        print('')
        
