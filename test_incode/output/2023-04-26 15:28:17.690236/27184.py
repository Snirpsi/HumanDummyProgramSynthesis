#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits and returns a list of words. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_removed = []
    
    while True:
        fruits_removed.append(fruits.pop(0))
        
        if fruits:
            print('The fruits are now ', fruits_removed)
        else:
            print('No more fruits.')
        
