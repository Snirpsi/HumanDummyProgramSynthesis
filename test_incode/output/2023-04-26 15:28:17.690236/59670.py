#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words. """    
    words = []
    with open('words.txt') as file:
        for line in file:
            words.append(line.strip())
    print(words)
    
