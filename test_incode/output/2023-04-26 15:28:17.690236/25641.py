#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits and returns a list of numbers. """    
    
    fruits = ['apple', 'orange', 'pear', 'banana', 'grape', 'mango']
    
    fruits_removed = remove_fruits(fruits)
    
    print(