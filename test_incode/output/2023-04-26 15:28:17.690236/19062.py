#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits. """    
    fruits = list('apple')
    while len(fruits):
        fruit = fruits.pop()
        if fruit == 'apple':
            fruits.remove('apple')
        else:
            print('{} is not an apple'.format(fruit))
            
