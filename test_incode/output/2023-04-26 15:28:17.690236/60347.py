#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input. """    
    
    # Open the file that contains the user input
    file = open('input.txt', 'r')
    
    # Read the file line by line
    for line in file:
        
        # Split the line into words
        words = line.split(' ')
        
        # Print the words in the file
        print(words)
        
        # Print the words that start with '