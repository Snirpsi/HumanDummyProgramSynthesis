#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits. """    
    while True:
        fruits = ['apple', 'banana', 'cherry']
        fruits.reverse()
        print('The fruits are:')
        for fruit in fruits:
            print(