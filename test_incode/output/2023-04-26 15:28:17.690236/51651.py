#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits and prints a list of numbers. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'cherry']
    
    while True:
        fruits.append(input('Enter a fruit: '))
        
        print('The fruit is: ', fruits[-1])
        
        if fruits[-1] == '