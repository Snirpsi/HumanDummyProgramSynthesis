#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or converts a list of numbers. """    
    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    
    while True:
        fruits = enumerate(fruits)
        
        for fruit in fruits:
            print('%s is %d 