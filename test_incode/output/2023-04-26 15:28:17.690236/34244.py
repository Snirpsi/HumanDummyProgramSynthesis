#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits or returns a list of words. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        word = input('Enter a word: ')
        
        if word in fruits:
            fruits.remove(word)
            
        else:
            print('No fruit named 