#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words or returns fruits. """    
    
    words = []
    
    while True:
        
        fruits = []
        
        while True:
            
            word = input('Enter a word: ')
            
            if word == 'quit':
                break
            
            fruits.append(word)
            
        print('\n'.join(