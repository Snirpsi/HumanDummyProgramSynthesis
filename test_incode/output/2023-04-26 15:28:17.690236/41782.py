#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
    words = ['foo', 'bar', 'baz', 'qux']
    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        
        if word in words:
            print(word)
        else:
            print('That word is not in the list')
            
    print('Goodbye!')
