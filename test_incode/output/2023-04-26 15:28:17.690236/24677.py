#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits and adds a port. """    
    fruits = ['apple', 'banana', 'cherry']
    port = 1
    while True:
        fruits.append(fruits.pop(0))
        print(