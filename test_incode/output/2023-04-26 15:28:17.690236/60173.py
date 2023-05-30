#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over fruits and iterates over all ports. """    
    fruits = ['apple', 'orange', 'mango', 'banana']
    ports = ['A', 'B', 'C', 'D']
    for fruit in fruits:
        for port in ports:
            print(fruit, port)
