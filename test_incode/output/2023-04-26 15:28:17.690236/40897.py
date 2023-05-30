#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores fruits and stores a list of words. """    
    fruits = ['apple', 'banana', 'cherry']
    words = ['apple', 'banana', 'cherry']
    
    fruits_set = set(fruits)
    words_set = set(words)
    
    print('Fruits:')
    print(fruits_set)
    
    print('Words:')
    print(words_set)
    
    print('Fruits and Words:')
    print(fruits_set & words_set)
    
    print('Fruits and Fruits:')
    print(fruits_set & fruits_set)
    
    print('Fruits and Fruits and Words:')
    print(fruits_set & fruits_set & words_set)
    
    print('Fruits and Fruits and Fruits:')
    print(fruits_set & fruits_set & fruits_set)
    
    print('Fruits and Fruits and Fruits and Words:')
    print(fruits_set & fruits_set & fruits_set & words_set)
    
    print('Fruits and Fruits and Fruits and Fruits:')
    print(fruits_set & fruits_set & fruits_set & fruits_set)
    
    print('Fruits and Fruits and Fruits and Fruits and Words:')
    print(fruits_set & fruits_set & fruits_set & fruits_set & words_set)
    
    print('Fruits and Fruits and Fruits and Fruits and Fruits and Words:')
    print(fruits_set & fruits_set & fruits_set & fruits_set & fruits_set & words_set)
    
    print('Fruits and Fruits and Fruits and Fruits and Fruits and Fruits and Words:')
    print(fruits_set & fruits_set & fruits_set & fruits_set & fruits_set & fruits_set & words_set)
    
    print('Fruits and Fruits and Fruits and Fruits and Fruits and Fruits and Fruits and Words:')
    print(fruits_set & fruits_set & fruits_set & fruits_set & fruits_set & fruits_set & fruits_set & words_set)
    
    print('Fruits and Fruits and Fruits and Fruits and Fruits and Fruits and Fruits and Fru