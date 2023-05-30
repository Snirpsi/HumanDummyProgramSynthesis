#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words and multiplyes fruits. """    
    words = []
    fruits = ['apple', 'orange', 'banana', 'pear']
    
    fruits_multiplied = []
    
    for fruit in fruits:
        fruits_multiplied.append(fruit*fruit)
        
    for word in words:
        words.append(word*fruits_multiplied[-1])
        
    print('\n'.join(words))
    
