#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        if word in words:
            print('The word "{}" is a palindrome.'.format(word))
        else:
            print('The word "{}" is not a palindrome.'.format(word))
            
        print('\n')
        
    print('Bye!')
    
