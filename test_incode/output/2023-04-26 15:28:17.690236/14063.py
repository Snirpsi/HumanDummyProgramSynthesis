#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or prints fruits. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'kiwi']
    while True:
        fruits = enumerate(fruits)
        print('\n'.join(map(str, fruits)))
