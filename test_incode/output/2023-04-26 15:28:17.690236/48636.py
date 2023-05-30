#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'snake', 'parrot', 'horse']
    
    word = ''
    
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        
        if word in words:
            print(word + ' is a word!')
        else:
            print(word + ' is not a word!')
            
        print('')
        
