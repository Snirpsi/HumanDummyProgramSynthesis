#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words and converts all ports. """    
    
    # Read all words from file
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Convert all words to ports
    ports = []
    for word in words:
        ports.append(word.split('-')[0])
    
    # Print all ports
    for port in ports:
        print('Port {} is {}'.format(port, 