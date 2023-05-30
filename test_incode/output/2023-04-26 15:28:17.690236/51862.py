#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers or prints fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    for fruit in fruits:
        print('{} is {}'.format(