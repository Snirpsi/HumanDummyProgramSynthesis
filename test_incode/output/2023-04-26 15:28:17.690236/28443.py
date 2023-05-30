#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Read the file line by line and append each line to a list
    for line in open('words.txt'):
        words.append(line.strip())
    
    # Return the list of words
    return 