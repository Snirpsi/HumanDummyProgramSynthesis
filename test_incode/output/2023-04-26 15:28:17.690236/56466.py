#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words. """    
    words = ['hello', 'world', '!']
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'exit':
            break
        
        if word in words:
            print('The word "{}" is a palindrome'.format(word))
        else:
            print('The word "{}" is not a palindrome'.format(word))
        
        print('')
        
