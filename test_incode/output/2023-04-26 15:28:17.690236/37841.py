#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or opens fruits. """    
    
    # Open the fruits.txt file as a text file
    fruits = open('fruits.txt', 'r')
    
    # Read each line of the text file
    for line in fruits:
        
        # Split the line into its constituent parts
        parts = line.strip().split()
        
        # Print the parts one by one
        print(' '.join(parts))
        
    # Close the text file
    fruits.close()
    
    # Close the program
    exit()
    
# End of program
