#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits and multiplyes a port. """    
    fruits = ['apple', 'banana', 'cherry']
    port = 2
    
    for fruit in fruits:
        print('Fruit {} multiplied by {} = {}'.format(fruit, port, fruit*port))
        port += 1
        
