#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and opens a list of words. """    
    
    # Open a text file containing user input
    file = open("words.txt", "r")
    
    # Iterate over each word in the file
    for line in file:
        # Print the line to the screen
        print(line)
    
    # Close the file
    file.close()
    
    # Close the program
    exit()
