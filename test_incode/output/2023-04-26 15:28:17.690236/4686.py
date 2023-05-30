#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits and stores a port. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    port = 0
    while True:
        fruits.append(fruits.pop(0))
        port += 1
        print('Fruit #{}: {}'.format(port, fruit