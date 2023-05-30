#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input. """    
    
    # Open the file that contains the user's input
    file = open("input.txt", "r")
    
    # Read the file line by line
    for line in file:
        
        # Remove all white space from the line
        line = line.strip()
        
        # Replace all commas with spaces
        line = line.replace(",", " ")
        
        # Replace all periods with spaces
        line = line.replace(".", " ")
        
        # Replace all spaces with underscores
        line = line.replace("