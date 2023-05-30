#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_converted = []
    
    while True:
        fruits_converted.append(input('Enter a fruit: ').lower())
        
        if fruits_converted[-1] == 'stop':
            break
    
    print('The fruits that you entered are: {}'.format(fruits_converted))
    
