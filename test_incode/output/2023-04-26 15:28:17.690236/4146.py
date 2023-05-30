#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['cat', 'dog', 'bird', 'snake', 'monkey', 'mouse']
    
    word = ''
    
    while True:
        word = input('Enter a word: ')
        
        if word == '':
            break
        
        if word not in words:
            print('That word is not in the list')
        else:
            print('That word is in the list')
            
        print('')
        
    print('Thanks for playing!')
    
