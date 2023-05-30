#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over fruits and multiplyes all ports. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'kiwi']
    ports = [1, 2, 3, 4, 5, 6]
    
    for fruit in fruits:
        for port in ports:
            print('{} x {}'.format(fruit, port))
    
