#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a port and iterates over fruits. """    
    port = 0
    fruits = ['apple', 'orange', 'banana', 'cherry']
    for fruit in fruits:
        port += 1
        print('Port {}: {}'.format(fruit, port