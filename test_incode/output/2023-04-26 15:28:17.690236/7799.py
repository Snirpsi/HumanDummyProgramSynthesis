#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = []
    
    # Read all words from file
    with open('words.txt', 'r') as f:
        lines = f.readlines()
        
    # Loop through each line
    for line in lines:
        line = line.strip()
        
        # Remove punctuation
        line = line.translate(None, '.,;:!?¿')
        
        # Remove whitespace
        line = line.strip()
        
        # Remove 