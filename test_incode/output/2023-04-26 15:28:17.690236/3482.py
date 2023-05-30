#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes all ports and iterates over fruits. """    
    
    ports = range(1,21)
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    for fruit in fruits:
        for port in ports:
            print('Port {} is {} and fruit is {}'.format(port, fruit