#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words. """    
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            print('Goodbye!')
            break
        
        if word in words:
            print('{} is a word'.format(word))
        else:
            print('{} is not a word'.format(word))
    
