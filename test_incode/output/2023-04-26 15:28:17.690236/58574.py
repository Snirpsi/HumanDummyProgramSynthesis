#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words or calculates words. """    
    while True:
        words = []
        
        # Read a line from the user
        line = input()
        
        # Remove any punctuation from the line
        line = line.translate(None, '.,;:!?