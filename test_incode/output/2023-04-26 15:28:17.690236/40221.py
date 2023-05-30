#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits and enumerates fruits. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    while True:
        fruits.sort()
        print('The fruit list is: ', fruits)
        print('The fruit enumerated is: ', enumerate(fruits))
        
