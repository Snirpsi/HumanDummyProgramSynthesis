#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words. """    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    # Print all words in file
    for word in words:
        print(word)
    
    # Print all words in file without spaces
    for word in words.