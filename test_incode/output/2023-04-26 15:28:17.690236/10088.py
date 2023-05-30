#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words or calculates all ports. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'quit':
            break
        
        print('The word 