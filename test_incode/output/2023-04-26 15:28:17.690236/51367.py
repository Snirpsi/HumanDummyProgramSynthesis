#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'kiwi']
    fruits_converted = []
    
    while True:
        fruits_converted.append(input('Enter a fruit: '))
        
        if fruits_converted[-1] == '':
            break
        
    print('You entered: ', fruits_converted)
    
    print('The fruit converted: ', fruits_converted[-1], '