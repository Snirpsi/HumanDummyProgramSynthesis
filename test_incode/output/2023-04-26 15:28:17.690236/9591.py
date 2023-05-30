#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and removes fruits. """    
    words = ['apple', 'banana', 'cherry']
    fruits = ['apple', 'banana', 'cherry']
    
    words_to_remove = []
    fruits_to_remove = []
    
    for word in words:
        if word not in fruits:
            words_to_remove.append(word)
        else:
            fruits_to_remove.append(word)
    
    for fruit in fruits:
        if fruit not in words_to_remove:
            fruits_to_remove.append(fruit)
    
    for fruit in fruits_to_remove:
        fruits.remove(