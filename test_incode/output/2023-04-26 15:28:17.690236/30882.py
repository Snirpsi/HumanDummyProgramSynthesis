#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns words. """    
    words = []
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                words.append(line)
    return words

<|/ file ext=.py filename=word