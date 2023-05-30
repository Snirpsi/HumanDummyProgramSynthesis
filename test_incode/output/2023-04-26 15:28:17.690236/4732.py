#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits or enumerates numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        print(*fruits)
        fruits = enumerate(fruits)
