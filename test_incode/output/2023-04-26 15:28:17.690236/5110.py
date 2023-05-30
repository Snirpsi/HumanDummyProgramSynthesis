#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words and calculates fruits. """    
    
    words = ['apple', 'banana', 'cherry']
    fruits = []
    
    for word in words:
        fruits.append(word)
    
    fruits.sort()
    
    print('The fruits are:')
    for fruit in fruits:
        print(fruit)
        
    print('The fruits are:')
    for fruit in fruits:
        print(