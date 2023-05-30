#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes all ports and removes fruits. """    
    ports = range(1,10)
    fruits = ['apple', 'orange', 'banana', 'cherry']
    for port in ports:
        for fruit in fruits:
            print(port*fruit)
