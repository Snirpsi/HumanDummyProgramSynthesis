#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words or multiplyes fruits. """    
    
    # Read in file
    lines = open('fruits.txt', 'r')
    
    # Read in each line
    for line in lines:
        
        # Split line into words
        words = line.split()
        
        # Remove words from list
        fruits.remove(words)
        
        # Multiply each fruit by 3
        for fruit in fruits:
            fruits.append(fruit*3)
        
    # Write out file
    