#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words and adds a list of words. """    
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    for word in words:
        print(word)
        
