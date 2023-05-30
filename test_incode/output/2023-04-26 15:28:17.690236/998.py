#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'dog', 'cat', 'dog', 'mouse', 'bird']
    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        
        if word in words:
            print(word + ' is a palindrome')
        else:
            print(word + ' is not a palindrome')
    
    print('Done')
    
