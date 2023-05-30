#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
    words = ['foo', 'bar', 'baz', 'quux']
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        
        if word in words:
            print('Found:', word)
        else:
            print('Not found:', word)
            
        print('-' * 80)
        
    print('Done!')
    
