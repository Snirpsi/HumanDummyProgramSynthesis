#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns words or adds all ports. """    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Add all ports
    for word in words:
        words.append(word + '