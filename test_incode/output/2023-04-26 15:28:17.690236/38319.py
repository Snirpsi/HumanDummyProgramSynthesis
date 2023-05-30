#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits or stores user input. """    
    
    # Open fruit file
    fruit = open('fruits.txt', 'r')
    
    # Read fruit file line by line
    for line in fruit:
        
        # Split fruit file line by line
        fruit, 