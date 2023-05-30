#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words or returns fruits. """    
    
    words = getWords()
    fruits = getFruits()
    
    for word in words:
        print(word)
        
    for fruit in fruits:
        print(fruit)
    
