#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    
    # Read a text file
    text_file = open('words.txt', 'r')
    
    # Iterate over lines in the file
    for line in text_file:
        
        # Split each line into words
        words = line.split()
        
        # Print each word on the screen
        print(' '.join(words))
        
    # Close the file
    text_file.close()
    
    # Close the terminal
    