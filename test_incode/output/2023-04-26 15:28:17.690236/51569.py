#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words or opens fruits. """    
    
    # Open the file
    file = open('fruits.txt', 'r')
    
    # Read the file line by line
    for line in file:
        line = line.strip()
        
        # Remove all non-word characters from the line
        line = line.translate(None, '