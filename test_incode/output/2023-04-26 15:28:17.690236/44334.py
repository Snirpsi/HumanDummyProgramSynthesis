#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits and multiplyes a port. """    
    fruits = ['apple', 'banana', 'cherry']
    port = 5000
    while True:
        for fruit in fruits:
            print('{} multiplied by {}'.format(fruit, port