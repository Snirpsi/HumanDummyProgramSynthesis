#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores user input or adds words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'q':
            break
    
    print('You entered', len(words), 'words')
    
    words = 