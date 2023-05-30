#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or stores words. """    
    
    fruits = ['apple', 'banana', 'cherry']
    words = []
    
    while True:
        fruits.append(input('Enter a fruit: '))
        words.append(input('Enter a word: '))
        
        if fruits == ['apple', 'banana', 'cherry']:
            break
        
    print('\nThe fruit 