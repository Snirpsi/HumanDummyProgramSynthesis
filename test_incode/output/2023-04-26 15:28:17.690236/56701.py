#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits. """    
    while True:
        fruits = ['apple', 'banana', 'cherry']
        fruits_multiplied = []
        for fruit in fruits:
            fruits_multiplied.append(fruit*2)
        print(*fruits_multiplied, sep='