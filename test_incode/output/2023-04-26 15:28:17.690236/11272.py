#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits. """    
    fruits = enumerate('apple', 'banana', 'orange', 'mango')
    for fruit in fruits:
        print(fruit)
