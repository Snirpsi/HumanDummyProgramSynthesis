#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits and converts a list of numbers. """    
    
    fruits = ['apple', 'orange', 'banana', 'pear', 'mango', 'grape', 'pineapple', 'kiwi']
    fruits_converted = [int(x) for x in fruits]
    
    print('fruits: ', fruits)
    print('fruits_converted: ', fruits_converted)
    
