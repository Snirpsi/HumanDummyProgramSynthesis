#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words and stores all ports. """    
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    ports = []
    for word in words:
        ports.append(