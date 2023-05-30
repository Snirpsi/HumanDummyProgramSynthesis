#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words and returns words. """    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    
    # Calculate words
    words = [