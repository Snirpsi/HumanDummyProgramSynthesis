#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words. """    
    words = ['cat', 'dog', 'bird', 'mouse']
    
    word = ''
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        if word not in words:
            print('That word is not in the list')
            continue
        
        print('That word is in the list')
        
        words.remove(word)
        
        print('The list now contains:')
        
        for word in words:
            print(word)
        
        print('\n')
        
        print('Would you like to enter another word? [y/N]')
        
        ans = input('(y/N) ')
        
        if ans == 'y':
            continue
        
        if ans == 'n':
            break
        
        print('That word was not in the list')
        
    print('Goodbye!')
