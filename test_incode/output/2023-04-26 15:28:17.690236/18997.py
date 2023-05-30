#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words. """    
    
    # Read input file
    file = open("words.txt", "r")
    lines = file.readlines()
    file.close()
    
    # Calculate list of words
    words = []
    for line in lines:
        words.append(line.strip().lower())
    
    # Print list of words
    print(words)
    
    # Close file
    file.close()
    
    # Close program
    exit(0)
    
