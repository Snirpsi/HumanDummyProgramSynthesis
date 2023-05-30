#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruits.append(input('Enter a fruit: '))
        print('You entered: ', fruits)
        
