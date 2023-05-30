#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        fruits.remove('cherry')
        
        print('Removed fruit {}'.format(fruit