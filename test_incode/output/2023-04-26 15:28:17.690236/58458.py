#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits and iterates over all ports. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        fruits.append(input('Enter a fruit: '))
        
        for fruit in fruits:
            print(