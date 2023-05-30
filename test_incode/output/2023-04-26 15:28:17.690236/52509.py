#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates fruits and adds user input. """    
    fruits = enumerate('apple', 'banana', 'cherry')
    for fruit in fruits:
        print('The fruit is', fruit)
        
