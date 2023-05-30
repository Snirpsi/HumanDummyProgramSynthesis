#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words. """    
    
    # Open the file
    file = open('words.txt', 'r')
    
    # Read the file line by line
    for line in file:
        # Print the line
        print(line)
    
    # Close the file
    file.close()
    
    # Close the program
    exit(0)
    
