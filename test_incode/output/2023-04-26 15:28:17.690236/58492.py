#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    while True:
        fruit = ''.join(random.choice(fruits) for x in range(