#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers or iterates over a list of numbers. """    
    
    # Open the file
    file = open('numbers.txt', 'r')
    
    # Iterate over the lines in the file
    for line in file:
        print(line)
        
    # Close the file
    file.close()
    
