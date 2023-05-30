#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits and multiplyes a port. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    port = 2
    while True:
        fruits.append(fruits.pop(0))
        port *= 2
        if fruits == []:
            break
    print('The fruits are {}'.format(fruits))
    print('The port is {}'.format(port))
