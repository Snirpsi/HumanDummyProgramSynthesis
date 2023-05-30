#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        
        if word in words:
            print('Found it!')
        else:
            print('Sorry, I don\'t know that word.')
        
        print('')
        
    print('Thanks for playing!')
    
