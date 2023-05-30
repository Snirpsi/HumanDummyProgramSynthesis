#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    
    # Open the word file.
    wordfile = open('words.txt', 'r')
    
    # Read each line of the word file.
    for line in wordfile:
        
        # Print each word on a new line.
        print(line.rstrip())
        
    # Close the word file.
    wordfile.close()
