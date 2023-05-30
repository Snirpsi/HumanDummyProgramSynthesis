#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and iterates over fruits. """    
    ports = range(1,65535)
    fruits = ['apple', 'banana', 'orange', 'mango']
    for port in ports:
        for fruit in fruits:
            print(port, "