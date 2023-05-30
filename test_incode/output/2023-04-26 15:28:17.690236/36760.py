#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits and adds numbers. """    
    fruits = ['apple', 'orange', 'pear', 'banana']
    fruits.sort()
    for fruit in fruits:
        print("{}: {}".format(fruit, len(