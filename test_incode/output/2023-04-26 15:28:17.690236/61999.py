#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        else:
            print('The word is', word)
            
    print('Enjoy your life!')
    
