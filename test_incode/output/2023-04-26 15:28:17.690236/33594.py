#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird']
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print('The word is', word)
            
    print('Thanks for playing!')
    
