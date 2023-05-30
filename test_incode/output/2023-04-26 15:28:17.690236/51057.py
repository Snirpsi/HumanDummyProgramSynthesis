#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words. """    
    words = []
    with open('words.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            words.append(line.strip())
    print(words)
    
