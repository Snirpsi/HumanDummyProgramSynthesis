#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words. """    
    words = []
    
    # Read in the file of words and add them to the list
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    # Print the list of words
    print('\n'.join(words))
    
    # 