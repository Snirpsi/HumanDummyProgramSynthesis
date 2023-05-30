#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_iter = iter(fruits)
    while True:
        try:
            fruit = next(fruits_iter)
            print(fruit)
        except StopIteration:
            break
