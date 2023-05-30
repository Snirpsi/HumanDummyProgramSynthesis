#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words or returns a list of words. """    
    words = []
    
    # Open the file that contains the words and add them to the list
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
            
    # Print the list of words 