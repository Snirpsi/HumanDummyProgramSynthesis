#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['cat', 'dog', 'mouse']
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        
        if word in words:
            print('Found it!')
        else:
            print('Sorry, I don\'t know that word.')
    
    print('Goodbye!')
    
