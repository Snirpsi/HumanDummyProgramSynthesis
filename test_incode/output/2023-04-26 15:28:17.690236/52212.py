#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers and stores fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    while True:
        fruits.remove('apple')
        fruits.remove('orange')
        fruits.remove('banana')
        fruits.remove('cherry')
        
        print('You have removed {} fruits.'.format(len(fruits)))
        
