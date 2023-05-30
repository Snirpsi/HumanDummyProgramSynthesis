#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words and iterates over all ports. """    
    
    words = []
    
    # Read all words from file
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Iterate over all ports
    for port in range(1, 65535):
        # Iterate over all words in port
        for word in words:
            # Print word on port 