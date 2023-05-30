#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words. """    
    
    # Open the file
    with open('words.txt') as file:
        # Iterate over the lines
        for line in file:
            # Split the line into words
            words = line.split(' ')
            # Print the word
            print(words)
            
