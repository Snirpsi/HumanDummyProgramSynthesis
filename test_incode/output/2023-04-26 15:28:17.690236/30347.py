#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or enumerates a list of numbers. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'grape', 'mango']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    while True:
        print("The fruit is:", fruits.pop(0))
        print("The number is:", numbers.pop(0))
        
