#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits and calculates numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits.sort()
    fruits_len = len(fruits)
    i = 0
    while i < fruits_len:
        print('Fruit #', i, 'is', fruits[i])
        i += 1
        
