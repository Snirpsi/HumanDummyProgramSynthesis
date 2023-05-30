#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits. """    
    
    # Open the fruits file
    fruits = open('fruits.txt', 'r')
    
    # Read each line of the fruits file
    for line in fruits:
        
        # Split the line into its individual words
        words = line.strip().split()
        
        # Print each word
        print(' '.join(words))
        
    # Close the fruits file
    fruits.close()
    
    # Close the terminal
    