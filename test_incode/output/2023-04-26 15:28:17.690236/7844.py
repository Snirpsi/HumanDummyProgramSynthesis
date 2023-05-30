#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits and converts a list of numbers. """    
    
    fruits = ['apple', 'banana', 'cherry', 'orange', 'pear']
    
    fruits_clean = remove_fruits(fruits)
    
    print(fruits_clean)
    
