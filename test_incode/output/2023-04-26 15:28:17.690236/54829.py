#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and adds a list of words. """    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        print('The word is', word)
        
        if word == 'q':
            break
        
    print('The words are', words)
    
