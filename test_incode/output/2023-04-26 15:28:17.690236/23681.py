#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates fruits or stores a list of numbers. """    
    fruits = ['apple', 'orange', 'banana', 'pear']
    fruits.sort()
    print(fruits)
    fruits.reverse()
    print(fruits)
    fruits.insert(1, 'peach')
    print(fruits)
    fruits.pop()
    print(fruits)
    fruits.pop(