#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words and stores a list of words. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'q':
            break
    
    print('The words are:')
    for word in words:
        print(word)
        
    print('Thanks for playing!')
    
