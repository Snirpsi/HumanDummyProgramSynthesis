#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers and removes fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_len = len(fruits)
    
    i = 0
    while i < fruits_len:
        if fruits[i] == 'cherry':
            fruits.pop(i)
        else:
            i += 1
            
    print(fruits)
    
