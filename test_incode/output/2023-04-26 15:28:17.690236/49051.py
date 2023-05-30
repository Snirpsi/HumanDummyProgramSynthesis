#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = []
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words.append(line)
    return words
