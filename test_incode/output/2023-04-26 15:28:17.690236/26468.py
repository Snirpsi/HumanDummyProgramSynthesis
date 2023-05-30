#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'done':
            break
        
    print('You entered:')
    for word in words:
        print(word)
        
    print('Done.')
    
