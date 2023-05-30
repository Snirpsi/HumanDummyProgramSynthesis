#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns fruits and iterates over a list of words. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'cherry']
    words = ['apple', 'orange', 'pear', 'banana', 'cherry']
    
    for fruit in fruits:
        for word in words:
            if fruit == word:
                print('{} is a fruit'.format(fruit))
            else:
                print('{} is not a fruit'.format(fruit))
                
